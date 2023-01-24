package main

type Permissions struct {
	canSeeMessages      bool
	canDeleteMessages   bool
	canEditMessages     bool
	canKickMembers      bool
	canMakeMembersAdmin bool
	canAddMembers       bool
}

func SetUserPermissions(permissions *Permissions) int8 {
	// TODO: Implement
	return 0
}

func GetUserPermissions(permissionsMask int8) *Permissions {
	// TODO: Implement
	return &Permissions{}
}
