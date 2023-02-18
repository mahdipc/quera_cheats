using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp1
{
    public class Program2
    {
        public static void Main2(string[] args)
        {
            var nd = (Console.ReadLine()).Split();
            var n = Convert.ToInt32(nd[0]);
            var d = Convert.ToInt64(nd[1]);

            var input = Console.ReadLine().Split();
            var ages = input.Select(age => Convert.ToInt64(age)).ToArray();

            var maxAge = ages.Max();


            var bag = ages.Select(item => maxAge - item - d).Where(item => item > 0).Sum();

            Console.Write(bag);

        }
    }
}
