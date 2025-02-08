package app

import (
	"errors"
	"time"

	"gorm.io/gorm"
)

type Repository struct {
	DB *gorm.DB
}

func (repo *Repository) CreateAttendance(attendance *Attendance) error {
	if _, exists := repo.IsExistDateAndProgrammerID(attendance.ProgrammerID, attendance.Date); exists {
		return errors.New("Duplicate attendance record")
	}
	if err := repo.DB.Create(attendance).Error; err != nil {
		return err
	}
	if attendance.ID == 0 {
		return errors.New("failed to create attendance record: generated ID is zero")
	}
	return nil
}

func (repo *Repository) GetAttendancesByProgrammer(pid uint) ([]Attendance, error) {
	var attendances []Attendance
	err := repo.DB.Where("programmer_id = ?", pid).Order("date desc").Limit(12).Find(&attendances).Error
	if err != nil {
		return nil, err
	}
	return attendances, nil
}

func (repo *Repository) GetAllAttendance() ([]Attendance, error) {
	var attendances []Attendance
	err := repo.DB.Find(&attendances).Error
	if err != nil {
		return nil, err
	}
	return attendances, nil
}

func (repo *Repository) UpdateAttendance(attendance *Attendance) error {
	var existing Attendance
	err := repo.DB.Where("programmer_id = ? AND date = ?", attendance.ProgrammerID, attendance.Date).First(&existing).Error
	if err != nil {
		return err
	}
	existing.Date = attendance.Date
	existing.CheckIn = attendance.CheckIn
	existing.CheckOut = attendance.CheckOut
	if err := repo.DB.Save(&existing).Error; err != nil {
		return err
	}
	return nil
}

func (repo *Repository) DeleteAttendance(pid uint) error {
	if err := repo.DB.Where("programmer_id = ?", pid).Delete(&Attendance{}).Error; err != nil {
		return err
	}
	return nil
}

func (repo *Repository) DeleteOneDayAttendance(pid uint, date time.Time) error {
	start := time.Date(date.Year(), date.Month(), date.Day(), 0, 0, 0, 0, date.Location())
	end := start.Add(24 * time.Hour)
	result := repo.DB.Where("programmer_id = ? AND date >= ? AND date < ?", pid, start, end).Delete(&Attendance{})
	if result.Error != nil {
		return result.Error
	}
	if result.RowsAffected == 0 {
		return errors.New("No attendance record found for the given date")
	}
	return nil
}

func (repo *Repository) GetGirinofReport(pid uint, date time.Time) (*GirinofReport, error) {
	start := time.Date(date.Year(), date.Month(), date.Day(), 0, 0, 0, 0, date.Location())
	end := start.Add(24 * time.Hour)
	var att Attendance
	err := repo.DB.Where("programmer_id = ? AND date >= ? AND date < ?", pid, start, end).First(&att).Error
	if err != nil {
		return nil, err
	}
	standardCheckIn := time.Date(att.Date.Year(), att.Date.Month(), att.Date.Day(), 9, 0, 0, 0, att.Date.Location())
	standardCheckOut := time.Date(att.Date.Year(), att.Date.Month(), att.Date.Day(), 17, 0, 0, 0, att.Date.Location())
	var delayMinutes int
	if att.CheckIn.After(standardCheckIn) {
		delayMinutes = int(att.CheckIn.Sub(standardCheckIn).Minutes())
	}
	var earlyDepartureMinutes int
	if att.CheckOut.Before(standardCheckOut) {
		earlyDepartureMinutes = int(standardCheckOut.Sub(att.CheckOut).Minutes())
	}
	report := &GirinofReport{ProgrammerID: pid, TotalDelays: delayMinutes, TotalEarlyDepartures: earlyDepartureMinutes}
	return report, nil
}

func (repo *Repository) GetMonthlyReport(pid uint, startDate, endDate time.Time) (*MonthlySummary, error) {
	var attendances []Attendance
	err := repo.DB.Where("programmer_id = ? AND date BETWEEN ? AND ?", pid, startDate, endDate).Find(&attendances).Error
	if err != nil {
		return nil, err
	}
	var totalDaysPresent int
	var totalOvertimeMinutes, totalDelayMinutes, totalEarlyDepartureMinutes int
	for _, att := range attendances {
		totalDaysPresent++
		standardCheckIn := time.Date(att.Date.Year(), att.Date.Month(), att.Date.Day(), 9, 0, 0, 0, att.Date.Location())
		standardCheckOut := time.Date(att.Date.Year(), att.Date.Month(), att.Date.Day(), 17, 0, 0, 0, att.Date.Location())
		if att.CheckIn.After(standardCheckIn) {
			totalDelayMinutes += int(att.CheckIn.Sub(standardCheckIn).Minutes())
		}
		if att.CheckOut.Before(standardCheckOut) {
			totalEarlyDepartureMinutes += int(standardCheckOut.Sub(att.CheckOut).Minutes())
		}
		if att.CheckOut.After(standardCheckOut) {
			totalOvertimeMinutes += int(att.CheckOut.Sub(standardCheckOut).Minutes())
		}
	}
	summary := &MonthlySummary{ProgrammerID: pid, TotalDaysPresent: totalDaysPresent, TotalOvertimeMinutes: totalOvertimeMinutes, TotalDelayMinutes: totalDelayMinutes, TotalEarlyDepartureMinutes: totalEarlyDepartureMinutes}
	return summary, nil
}

func (repo *Repository) CalculateSalary(pid uint, startDate, endDate time.Time) (*SalaryReport, error) {
	programmer, err := repo.GetProgrammerByID(pid)
	if err != nil {
		return nil, err
	}
	var attendances []Attendance
	err = repo.DB.Where("programmer_id = ? AND date BETWEEN ? AND ?", pid, startDate, endDate).Find(&attendances).Error
	if err != nil {
		return nil, err
	}
	var totalDaysPresent int
	var totalOvertimeMinutes, totalDelayMinutes, totalEarlyDepartureMinutes int
	for _, att := range attendances {
		totalDaysPresent++
		standardCheckIn := time.Date(att.Date.Year(), att.Date.Month(), att.Date.Day(), 9, 0, 0, 0, att.Date.Location())
		standardCheckOut := time.Date(att.Date.Year(), att.Date.Month(), att.Date.Day(), 17, 0, 0, 0, att.Date.Location())
		if att.CheckIn.After(standardCheckIn) {
			totalDelayMinutes += int(att.CheckIn.Sub(standardCheckIn).Minutes())
		}
		if att.CheckOut.Before(standardCheckOut) {
			totalEarlyDepartureMinutes += int(standardCheckOut.Sub(att.CheckOut).Minutes())
		}
		if att.CheckOut.After(standardCheckOut) {
			totalOvertimeMinutes += int(att.CheckOut.Sub(standardCheckOut).Minutes())
		}
	}
	dailyRate := 100.0
	overtimeRate := 20.0
	delayPenalty := 10.0
	baseSalary := float64(totalDaysPresent) * dailyRate
	overtimePay := float64(totalOvertimeMinutes) * overtimeRate
	delayPenaltyAmount := float64(totalDelayMinutes) * delayPenalty
	totalSalary := baseSalary + overtimePay - delayPenaltyAmount
	report := &SalaryReport{Name: programmer.Name, TotalDaysPresent: totalDaysPresent, TotalOvertimeMinutes: totalOvertimeMinutes, TotalDelayMinutes: totalDelayMinutes, TotalEarlyDepartureMinutes: totalEarlyDepartureMinutes, TotalSalary: totalSalary}
	return report, nil
}

func (repo *Repository) CreateProgrammer(name string) (*Programmer, error) {
	if name == "" {
		return nil, errors.New("Name is required")
	}
	programmer := &Programmer{Name: name}
	if err := repo.DB.Create(programmer).Error; err != nil {
		return nil, err
	}
	if programmer.ID == 0 {
		return nil, errors.New("failed to create programmer: generated ID is zero")
	}
	return programmer, nil
}

func (repo *Repository) GetProgrammerByID(id uint) (*Programmer, error) {
	var programmer Programmer
	err := repo.DB.First(&programmer, id).Error
	if err != nil {
		return nil, err
	}
	return &programmer, nil
}

func (repo *Repository) IsExistDateAndProgrammerID(pid uint, date time.Time) (*Attendance, bool) {
	start := time.Date(date.Year(), date.Month(), date.Day(), 0, 0, 0, 0, date.Location())
	end := start.Add(24 * time.Hour)
	var att Attendance
	err := repo.DB.Where("programmer_id = ? AND date >= ? AND date < ?", pid, start, end).First(&att).Error
	if err != nil {
		if errors.Is(err, gorm.ErrRecordNotFound) {
			return nil, false
		}
		return nil, false
	}
	return &att, true
}
