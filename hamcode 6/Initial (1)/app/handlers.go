package app

import (
	"encoding/json"
	"net/http"
	"strconv"
	"strings"
	"time"
)

var Repo *Repository

func CreateAttendanceHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	var att Attendance
	if err := json.NewDecoder(r.Body).Decode(&att); err != nil {
		http.Error(w, "Invalid input format", http.StatusBadRequest)
		return
	}
	if att.Date.IsZero() {
		http.Error(w, "Missing required field: date", http.StatusBadRequest)
		return
	}
	if att.CheckOut.Before(att.CheckIn) {
		http.Error(w, "CheckOut cannot be before CheckIn", http.StatusBadRequest)
		return
	}
	if _, err := Repo.GetProgrammerByID(att.ProgrammerID); err != nil {
		http.Error(w, "Programmer not found! Please hire the programmer first", http.StatusNotFound)
		return
	}
	if err := Repo.CreateAttendance(&att); err != nil {
		http.Error(w, "Failed to create attendance: "+err.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(att)
}

func GetAllAttendanceHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	atts, err := Repo.GetAllAttendance()
	if err != nil {
		http.Error(w, "Failed to fetch attendance records: "+err.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(atts)
}

func GetAttendanceHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	parts := strings.Split(r.URL.Path, "/")
	if len(parts) < 3 {
		http.Error(w, "Invalid Programmer ID", http.StatusBadRequest)
		return
	}
	pid, err := strconv.ParseUint(parts[2], 10, 64)
	if err != nil || pid < 1 {
		http.Error(w, "Invalid Programmer ID", http.StatusBadRequest)
		return
	}
	atts, err := Repo.GetAttendancesByProgrammer(uint(pid))
	if err != nil {
		http.Error(w, "Error retrieving attendance records: "+err.Error(), http.StatusInternalServerError)
		return
	}
	if len(atts) == 0 {
		http.Error(w, "No attendance records found for the given Programmer ID", http.StatusNotFound)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(atts)
}

func UpdateAttendanceHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPut {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	parts := strings.Split(r.URL.Path, "/")
	if len(parts) < 3 {
		http.Error(w, "Invalid Programmer ID", http.StatusBadRequest)
		return
	}
	pid, err := strconv.ParseUint(parts[2], 10, 64)
	if err != nil || pid < 1 {
		http.Error(w, "Invalid Programmer ID", http.StatusBadRequest)
		return
	}
	if _, err := Repo.GetProgrammerByID(uint(pid)); err != nil {
		http.Error(w, "Programmer not found", http.StatusNotFound)
		return
	}
	var inp struct {
		Date     string `json:"date"`
		CheckIn  string `json:"check_in"`
		CheckOut string `json:"check_out"`
	}
	if err := json.NewDecoder(r.Body).Decode(&inp); err != nil {
		http.Error(w, "Invalid input format", http.StatusBadRequest)
		return
	}
	if inp.Date == "" {
		http.Error(w, "Date is required", http.StatusBadRequest)
		return
	}
	dt, err := time.Parse("2006-01-02", inp.Date)
	if err != nil {
		http.Error(w, "invalid date format, expected YYYY-MM-DD", http.StatusBadRequest)
		return
	}
	var ci, co time.Time
	if inp.CheckIn != "" {
		ci, err = time.Parse("2006-01-02 15:04:05", inp.CheckIn)
		if err != nil {
			http.Error(w, "invalid check_in/check_out format, expected YYYY-MM-DD HH:MM:SS", http.StatusBadRequest)
			return
		}
	}
	if inp.CheckOut != "" {
		co, err = time.Parse("2006-01-02 15:04:05", inp.CheckOut)
		if err != nil {
			http.Error(w, "invalid check_in/check_out format, expected YYYY-MM-DD HH:MM:SS", http.StatusBadRequest)
			return
		}
	}
	if !ci.IsZero() && !co.IsZero() && ci.After(co) {
		http.Error(w, "CheckIn cannot be after CheckOut", http.StatusBadRequest)
		return
	}
	att := Attendance{ProgrammerID: uint(pid), Date: dt, CheckIn: ci, CheckOut: co}
	if err := Repo.UpdateAttendance(&att); err != nil {
		http.Error(w, "Failed to update attendance: "+err.Error(), http.StatusInternalServerError)
		return
	}
	rep, err := Repo.GetGirinofReport(uint(pid), dt)
	if err != nil {
		http.Error(w, "Failed to generate report: "+err.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(rep)
}

func DeleteAttendanceHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodDelete {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	parts := strings.Split(r.URL.Path, "/")
	if len(parts) < 3 {
		http.Error(w, "Invalid programmer ID", http.StatusBadRequest)
		return
	}
	pid, err := strconv.ParseUint(parts[2], 10, 64)
	if err != nil || pid < 1 {
		http.Error(w, "Invalid programmer ID", http.StatusBadRequest)
		return
	}
	if _, err := Repo.GetProgrammerByID(uint(pid)); err != nil {
		http.Error(w, "Programmer not found", http.StatusNotFound)
		return
	}
	if err := Repo.DeleteAttendance(uint(pid)); err != nil {
		http.Error(w, "Failed to delete attendance: "+err.Error(), http.StatusInternalServerError)
		return
	}
	w.WriteHeader(http.StatusAccepted)
}

func DeleteOneDayAttendanceHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodDelete {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	parts := strings.Split(r.URL.Path, "/")
	if len(parts) < 4 {
		http.Error(w, "Invalid request", http.StatusBadRequest)
		return
	}
	pid, err := strconv.ParseUint(parts[2], 10, 64)
	if err != nil || pid < 1 {
		http.Error(w, "Invalid programmer ID", http.StatusBadRequest)
		return
	}
	dt, err := time.Parse("2006-01-02", parts[3])
	if err != nil {
		http.Error(w, "Invalid Date", http.StatusBadRequest)
		return
	}
	if _, err := Repo.GetProgrammerByID(uint(pid)); err != nil {
		http.Error(w, "Programmer not found", http.StatusNotFound)
		return
	}
	if err := Repo.DeleteOneDayAttendance(uint(pid), dt); err != nil {
		http.Error(w, "Failed to delete attendance: "+err.Error(), http.StatusInternalServerError)
		return
	}
	w.WriteHeader(http.StatusAccepted)
}

func GetGirinofReportHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	parts := strings.Split(r.URL.Path, "/")
	if len(parts) < 4 {
		http.Error(w, "Invalid request", http.StatusBadRequest)
		return
	}
	pid, err := strconv.ParseUint(parts[2], 10, 64)
	if err != nil || pid < 1 {
		http.Error(w, "Invalid Programmer ID", http.StatusBadRequest)
		return
	}
	dt, err := time.Parse("2006-01-02", parts[3])
	if err != nil {
		http.Error(w, "Invalid Date", http.StatusBadRequest)
		return
	}
	if _, err := Repo.GetProgrammerByID(uint(pid)); err != nil {
		http.Error(w, "Programmer not found", http.StatusNotFound)
		return
	}
	rep, err := Repo.GetGirinofReport(uint(pid), dt)
	if err != nil {
		http.Error(w, "Programmer with the given date not recorded. Please use CreateAttendanceHandler to create it!", http.StatusBadRequest)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(rep)
}

func GetMonthlyReportHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	parts := strings.Split(r.URL.Path, "/")
	if len(parts) < 6 {
		http.Error(w, "Invalid request", http.StatusBadRequest)
		return
	}
	pid, err := strconv.ParseUint(parts[3], 10, 64)
	if err != nil || pid < 1 {
		http.Error(w, "Invalid programmer ID", http.StatusBadRequest)
		return
	}
	startDt, err := time.Parse("2006-01-02", parts[4])
	if err != nil {
		http.Error(w, "Invalid start date format", http.StatusBadRequest)
		return
	}
	endDt, err := time.Parse("2006-01-02", parts[5])
	if err != nil {
		http.Error(w, "Invalid end date format", http.StatusBadRequest)
		return
	}
	if endDt.Before(startDt) {
		http.Error(w, "End date cannot be before start date", http.StatusBadRequest)
		return
	}
	if _, err := Repo.GetProgrammerByID(uint(pid)); err != nil {
		http.Error(w, "Programmer not found", http.StatusNotFound)
		return
	}
	sum, err := Repo.GetMonthlyReport(uint(pid), startDt, endDt)
	if err != nil {
		http.Error(w, "Failed to generate monthly report: "+err.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(sum)
}

func GetSalaryHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	parts := strings.Split(r.URL.Path, "/")
	if len(parts) < 3 {
		http.Error(w, "Invalid programmer ID", http.StatusBadRequest)
		return
	}
	pid, err := strconv.ParseUint(parts[2], 10, 64)
	if err != nil || pid < 1 {
		http.Error(w, "Invalid programmer ID", http.StatusBadRequest)
		return
	}
	if _, err := Repo.GetProgrammerByID(uint(pid)); err != nil {
		http.Error(w, "Programmer not found", http.StatusNotFound)
		return
	}
	now := time.Now()
	startDt := now.AddDate(0, 0, -30)
	rep, err := Repo.CalculateSalary(uint(pid), startDt, now)
	if err != nil {
		http.Error(w, "Failed to calculate salary: "+err.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(rep)
}

func CreateProgrammerHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	var inp ProgrammerInput
	if err := json.NewDecoder(r.Body).Decode(&inp); err != nil {
		http.Error(w, "Invalid input format", http.StatusBadRequest)
		return
	}
	if inp.Name == "" {
		http.Error(w, "Name is required", http.StatusBadRequest)
		return
	}
	prog, err := Repo.CreateProgrammer(inp.Name)
	if err != nil {
		http.Error(w, "Failed to create programmer: "+err.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(prog)
}
