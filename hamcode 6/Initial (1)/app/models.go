package app

import (
	"encoding/json"
	"errors"
	"time"
)

func (a *Attendance) UnmarshalJSON(data []byte) error {
	var aux struct {
		ProgrammerID uint   `json:"programmer_id"`
		Date         string `json:"date"`
		CheckIn      string `json:"check_in"`
		CheckOut     string `json:"check_out"`
	}
	if err := json.Unmarshal(data, &aux); err != nil {
		return err
	}
	dt, err := time.Parse("2006-01-02", aux.Date)
	if err != nil {
		return errors.New("expected YYYY-MM-DD")
	}
	ci, err := time.Parse("2006-01-02 15:04:05", aux.CheckIn)
	if err != nil {
		return errors.New("expected YYYY-MM-DD HH:MM:SS")
	}
	co, err := time.Parse("2006-01-02 15:04:05", aux.CheckOut)
	if err != nil {
		return errors.New("expected YYYY-MM-DD HH:MM:SS")
	}
	a.ProgrammerID = aux.ProgrammerID
	a.Date = dt
	a.CheckIn = ci
	a.CheckOut = co
	return nil
}

func (a Attendance) MarshalJSON() ([]byte, error) {
	type attOut struct {
		ID           uint   `json:"id"`
		ProgrammerID uint   `json:"programmer_id"`
		Date         string `json:"date"`
		CheckIn      string `json:"check_in"`
		CheckOut     string `json:"check_out"`
	}
	out := attOut{
		ID:           a.ID,
		ProgrammerID: a.ProgrammerID,
		Date:         a.Date.Format("2006-01-02"),
		CheckIn:      a.CheckIn.Format("2006-01-02 15:04:05"),
		CheckOut:     a.CheckOut.Format("2006-01-02 15:04:05"),
	}
	return json.Marshal(out)
}

func (ai *AttendanceInput) UnmarshalJSON(data []byte) error {
	var raw struct {
		Date     string  `json:"date"`
		CheckIn  *string `json:"check_in"`
		CheckOut *string `json:"check_out"`
	}
	if err := json.Unmarshal(data, &raw); err != nil {
		return err
	}
	if raw.Date == "" {
		return errors.New("date field is necessary")
	}
	dt, err := time.Parse("2006-01-02", raw.Date)
	if err != nil {
		return errors.New("invalid date format, expected YYYY-MM-DD")
	}
	ai.Date = dt
	if raw.CheckIn != nil {
		ci, err := time.Parse("2006-01-02 15:04:05", *raw.CheckIn)
		if err != nil {
			return errors.New("invalid check_in/check_out format, expected YYYY-MM-DD HH:MM:SS")
		}
		ai.CheckIn = &ci
	} else {
		ai.CheckIn = nil
	}
	if raw.CheckOut != nil {
		co, err := time.Parse("2006-01-02 15:04:05", *raw.CheckOut)
		if err != nil {
			return errors.New("invalid check_in/check_out format, expected YYYY-MM-DD HH:MM:SS")
		}
		ai.CheckOut = &co
	} else {
		ai.CheckOut = nil
	}
	return nil
}
