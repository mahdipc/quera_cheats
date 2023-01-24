package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestGetUserPermissionsSample(t *testing.T) {
	assert.Equal(t, &Permissions{
		canSeeMessages:      true,
		canDeleteMessages:   false,
		canEditMessages:     false,
		canKickMembers:      false,
		canMakeMembersAdmin: false,
		canAddMembers:       false,
	}, GetUserPermissions(1))
}

func TestSetUserPermissionsSample(t *testing.T) {
	assert.Equal(t, int8(1), SetUserPermissions(&Permissions{
		canSeeMessages:      true,
		canDeleteMessages:   false,
		canEditMessages:     false,
		canKickMembers:      false,
		canMakeMembersAdmin: false,
		canAddMembers:       false,
	}))
}
