import React from 'react'
import users from './users.json'
import UserItem from './UserItem'
import AverageAge from './AverageAge'
const UserList = () => {
  const users = users.filter((user) => user.role === 'user')
  const admins = users.filter((user) => user.role === 'admin')
  const sum = admins.reduce((acc, cur) => {
    return acc + cur.age
  }, 0)
  const avg = sum / admins.length

  return (
    <div>
      {users.map((user) => (
        <UserItem name={user.name} />
      ))}
      <AverageAge average={avg} />
    </div>
  )
}

export default UserList
