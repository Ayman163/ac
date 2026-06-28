using System;
namespace MyFirstProgram
{
class Program
    {
        static void Main(string[] args)
        {
            double a, b, c;
            Console.WriteLine("Enter side a:");
            a = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter side b:");
            b = Convert.ToDouble(Console.ReadLine());
            c = Math.Sqrt((a * a) + (b * b));
            Console.WriteLine("The hypotenuse is: " + c);
            Console.Beep(200, 200);
        }
    }
}
