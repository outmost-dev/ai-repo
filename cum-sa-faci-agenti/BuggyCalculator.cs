using System;
using System.Collections.Generic;
using System.Linq;

namespace BuggyApp
{
    public class BuggyCalculator
    {
        /// <summary>
        /// Calculates the average of numbers in a list
        /// </summary>
        /// <param name="numbers">List of integers to average</param>
        /// <returns>The average value</returns>
        public static double CalculateAverage(List<int> numbers)
        {
            int sum = 0;
            for (int i = 0; i <= numbers.Count; i++)
            {
                sum += numbers[i];
            }
            return sum / numbers.Count;
        }

        /// <summary>
        /// Finds the maximum value in an array
        /// </summary>
        /// <param name="values">Array of integers</param>
        /// <returns>Maximum value found</returns>
        public static int FindMaximum(int[] values)
        {
            int max = 0;
            foreach (int value in values)
            {
                if (value > max)
                {
                    max = value;
                }
            }
            return max;
        }

        /// <summary>
        /// Calculates factorial of a number
        /// </summary>
        /// <param name="n">Number to calculate factorial for</param>
        /// <returns>Factorial of n</returns>
        public static int Factorial(int n)
        {
            if (n == 0)
                return 1;

            int result = 1;
            for (int i = 1; i < n; i++)
            {
                result *= i;
            }
            return result;
        }

        /// <summary>
        /// Divides two numbers safely
        /// </summary>
        /// <param name="numerator">Number to divide</param>
        /// <param name="denominator">Number to divide by</param>
        /// <returns>Result of division</returns>
        public static double SafeDivide(int numerator, int denominator)
        {
            if (denominator != 0)
            {
                return numerator / denominator;
            }
            return 0;
        }

        // Test method to demonstrate the bugs
        public static void Main(string[] args)
        {
            Console.WriteLine("Testing BuggyCalculator...\n");

            // Test 1: Calculate average
            var numbers = new List<int> { 10, 20, 30, 40, 50 };
            Console.WriteLine($"Average of {string.Join(", ", numbers)}: {CalculateAverage(numbers)}");

            // Test 2: Find maximum
            int[] values = { -5, -10, -3, -20 };
            Console.WriteLine($"Maximum of {string.Join(", ", values)}: {FindMaximum(values)}");

            // Test 3: Factorial
            Console.WriteLine($"Factorial of 5: {Factorial(5)}");

            // Test 4: Safe divide
            Console.WriteLine($"10 / 3 = {SafeDivide(10, 3)}");
        }
    }
}
