using System;

namespace ConsoleApp1
{
    public class Program1
    {
        public static void Main1(string[] args)
        {
            var input = Console.ReadLine();
            var n = Convert.ToInt32(input);
            input = Console.ReadLine();
            var m = Convert.ToInt32(input);
            if ((n == 1 && m == 4) || (n == 4 && m == 1) || (n == 2 && m == 3) || (n == 3 && m == 2))
            {
                Console.Write(2);

            }
            else if (n == m)
                Console.Write(0);

            else
            {
                Console.Write(1);

            }


        }
    }
}
