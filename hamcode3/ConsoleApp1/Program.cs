using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Threading;

namespace ConsoleApp1
{
    public enum RoleEn
    {
        ADMIN,
        MENTOR,
        MEMBER
    }
    public class User
    {
        public string UserName { get; set; }
        public string Role { get; set; }
        public bool IsActive { get; set; }
        public bool IsQue { get; set; }
    }
    public class Program
    {
        public static IList<User> Users { get; set; }
        public static void Register(string userName, string role)
        {
            if (Users != null && Users.Any(x => x.UserName == userName))
            {
                Console.WriteLine("INVALID USERNAME");
                return;
            }

            if (role == "ADMIN" || role == "MENTOR" || role == "MEMBER")
            {
                if (Users == null)
                {
                    Users = new List<User>();
                }
                Users.Add(new User
                {

                    UserName = userName,
                    Role = role,
                    IsActive = false,
                    IsQue = true
                });
                Console.WriteLine("WAITING FOR ACCEPT");
            }
            else
            {
                Console.WriteLine("INVALID ROLE");
            }
        }

        public static void Approve(string userName1, string userName2)
        {
            var user1 = Users.FirstOrDefault(x => x.UserName == userName1);
            var user2 = Users.FirstOrDefault(x => x.UserName == userName2);
            if (user1 == null)
            {
                Console.WriteLine("INVALID USERNAME");
                return;
            }

            if (user1.IsActive == false)
            {

                Console.WriteLine("WAITING FOR ADMIN");
                return;
            }
            if (user1.Role != "ADMIN")
            {
                Console.WriteLine(userName1 + "IS NOT ADMIN");
                return;
            }
            if (user2 == null)
            {
                Console.WriteLine("INVALID USERNAME");
                return;
            }
            if (user2.IsActive == true)
            {
                Console.WriteLine(userName2 + "IS ACTIVE");
                return;
            }
            user2.IsQue = false;
            Console.WriteLine(userName2 + "REJECTED");

        }

        public static void ChangeRole(string userName1, string userName2, string role)
        {
            var user1 = Users.FirstOrDefault(x => x.UserName == userName1);
            var user2 = Users.FirstOrDefault(x => x.UserName == userName2);
            if (user1 == null || user2 == null)
            {
                Console.WriteLine("INVALID USERNAME");
                return;
            }
            if (user1.IsActive == false || user2.IsActive == false)
            {

                Console.WriteLine("WAITING FOR ADMIN");
                return;
            }
            if (!(role == "ADMIN" || role == "MENTOR" || role == "MEMBER"))
            {

                Console.WriteLine("INVALID ROLE");
            }

            if (user1.Role == user2.Role)
            {
                Console.WriteLine("NOT ENOUGH ACCESS");
            }
        }

        public static void Reject(string userName1, string userName2)
        {
            var user1 = Users.FirstOrDefault(x => x.UserName == userName1);
            var user2 = Users.FirstOrDefault(x => x.UserName == userName2);
            if (user1 == null)
            {
                Console.WriteLine("INVALID USERNAME");
                return;
            }

            if (user1.IsActive == false)
            {

                Console.WriteLine("WAITING FOR ADMIN");
                return;
            }
            if (user1.Role != "ADMIN")
            {
                Console.WriteLine(userName1 + "IS NOT ADMIN");
                return;
            }
            if (user2 == null)
            {
                Console.WriteLine("INVALID USERNAME");
                return;
            }
            if (user2.IsActive == true)
            {
                Console.WriteLine(userName2 + "IS ACTIVE");
                return;
            }
            user2.IsActive = false;

        }

        public static void Queue(string userName)
        {
            var user1 = Users.FirstOrDefault(x => x.UserName == userName);
            if (user1 == null)
            {
                Console.WriteLine("INVALID USERNAME");
                return;
            }
            if (user1.IsActive == false)
            {

                Console.WriteLine("WAITING FOR ADMIN");
                return;
            }
            if (user1.Role != "MEMBER")
            {
                Console.WriteLine("NOT ENOUGH ACCESS");
                return;
            }

            var model = Users.Where(x => x.IsActive == false && x.IsQue == true)
                .OrderBy(x => x.UserName)
                .ToList();
            if (model.Count == 0)
            {
                Console.WriteLine("NO USER");
                return;
            }

            Console.Write(string.Join(" ", model.Select(x => x.UserName)));
        }

        public static void Main(string[] args)
        {
            var n = Convert.ToInt32(Console.ReadLine());

            var sList = new List<string>();
            for (int i = 0; i < n; i++)
            {
                var t = Console.ReadLine();
                sList.Add(t);
            }

            foreach (var t in sList)
            {

                if (t.StartsWith("REGISTER "))
                {
                    var values = t.Split();
                    Register(values[1], values[2]);
                }
                else if (t.StartsWith("APPROVE "))
                {

                    var values = t.Split();
                    Approve(values[1], values[2]);
                }
                else if (t.StartsWith("REJECT "))
                {

                    var values = t.Split();
                    Reject(values[1], values[2]);
                }
                else if (t.StartsWith("QUEUE "))
                {

                    var values = t.Split();
                    Queue(values[1]);
                }
                else if (t.StartsWith("CHANGEROLE "))
                {

                    var values = t.Split();
                    ChangeRole(values[1], values[2], values[3]);
                }
            }

        }
    }
}
