package the_lib

import (
	"errors"
	str "strings"
)

type Data struct{}

func LoadData() (*Data, error) {
	return nil, errors.New("there is no path to load data")
}

func LoadDataWithPath(path string) (*Data, error) {
	if len(path) < 10 {
		return nil, errors.New("path is too short")
	} else if len(path) >= 256 {
		return nil, errors.New("path is too long")
	} else if str.ToLower(path) != path {
		return nil, errors.New("path should be all lowercase")
	} else if str.HasPrefix(path, "/") {
		return nil, errors.New("path should be relative")
	} else if str.TrimSpace(path) != path {
		return nil, errors.New("path should be trimmed")
	} else if str.Contains(path, "..") {
		return nil, errors.New("path should not retreat")
	} else {
		return &Data{}, nil
	}
}

func (data *Data) Manipulate(anotherData *Data) error {
	if anotherData == nil {
		return errors.New("another data should not be nil")
	} else if data == anotherData {
		return errors.New("cannot manipulate same data")
	} else {
		return nil
	}
}
