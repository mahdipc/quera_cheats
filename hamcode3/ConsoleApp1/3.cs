using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp1
{
    public class Program3
    {
        public static void Main3(string[] args)
        {
            var sList = new List<string>();
            var t = Convert.ToInt32(Console.ReadLine());
            for (var i = 0; i < t; i++)
            {
                var s = Console.ReadLine();
                sList.Add(s);
            }

            foreach (var s in sList)
            {
                long i = 0;
                var charsOrder = s.Select(x => new
                {
                    index = ++i,
                    charechter = x.ToString(),
                }).OrderBy(x => x.charechter)
                    .Reverse()
                    .Select(x => x.index);
                Console.WriteLine(string.Join(" ", charsOrder));
            }


        }
    }
}
