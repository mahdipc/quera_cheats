namespace ConsoleApp
{
    public class Program
    {
        static void Main(string[] args)
        {
            var textReplacer = new TextReplacer("@");

            // template data
            textReplacer.AddTag("humanName", "Timmy");

            string inputText = "Hello, my name is @humanName, and I love @color.";

            string resultText = textReplacer.ReplaceTags(inputText);
            Console.WriteLine(resultText);
        }

        public static bool YourAction()
        {
            return true;
        }
    }
}
