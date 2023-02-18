using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;

namespace ConsoleApp1
{
    public class Program5
    {

        public static void Main5(string[] args)
        {
            var n = 100;
            var sList = new List<int>();
            for (int i = 0; i < n; i++)
            {
                var t = Console.ReadLine();
                if (t.Any(x => x != '.'))
                {
                    var start = false;
                    var end = false;

                    sList.Add(t.Count(x => x != '.'));
                }
            }

            var a = sList.Count(x => x == sList.Max());
            var b = sList.Count(x => x == sList.Min());
            var c = sList.Count(x => x != sList.Max() && x != sList.Min());
            if (b == 3)
            {
                Console.WriteLine("B");

            }
            else if (a == 1)
            {
                Console.WriteLine("A");
            }
            else
            {
                Console.WriteLine("C");
            }


        }
    }
}
