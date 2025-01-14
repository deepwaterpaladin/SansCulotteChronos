# Building a Date Converter for the French Revolutionary Calendar
The French Revolutionary Calendar, introduced during the French Revolution in 1793, aimed to break from traditional religious and royalist conventions. This calendar featured 12 months of 30 days each, with five or six complementary days at the end of the year, known as Sans-culottides. This project recreates the conversion between the Gregorian calendar and the Revolutionary Calendar as a Python console application, using the rich library for a polished user interface.

## Project Overview
The main goal was to design a user-friendly application capable of:
- Converting any Gregorian date to its Revolutionary equivalent.
- Converting a Revolutionary date back to the Gregorian calendar.
- Displaying today's date on the Revolutionary Calendar.
The application employs Python's datetime module for date manipulations and rich for a clean, interactive console experience. The Revolutionary Calendar logic is based on its official start date: September 22, 1792.

## Code Walkthrough
The program begins by defining constants, including the start date and the names of the Revolutionary months. It includes two main conversion functions:
- Gregorian to Revolutionary: Calculates the year, month, and day in the Revolutionary Calendar based on the difference in days from its start date.
- Revolutionary to Gregorian: Computes the corresponding Gregorian date by reversing the above logic.
- A menu-driven interface lets users select tasks, with prompts ensuring error-free input.

## Challenges and Solutions
  1. Handling Leap Years and Edge Cases
    The Revolutionary Calendar approximates the solar year, but its leap-year rules differ from the Gregorian system. Implementing this accurately required careful adjustments for the extra days during Sans-culottides.

    Solution: For simplicity, this implementation assumes a 365-day year without adjusting for Revolutionary leap years. Future iterations could refine this with historical rules.

  3. User Input Validation
    Accepting Revolutionary dates in various formats, including handling invalid months or days, required robust error checking.
    
    Solution: The program validates inputs by ensuring the month exists in the predefined list and days fall within valid ranges.
  
  3. Maintaining Historical Fidelity
    Staying true to the original structure of the calendar while ensuring practical usability posed a challenge.
    
    Solution: The application avoids approximations like aligning Revolutionary months with Gregorian months, ensuring the output reflects the historical calendar structure.

## Conclusion
This date converter bridges the gap between history and modern technology, allowing users to explore the unique French Revolutionary Calendar. With a user-friendly rich-powered interface and flexible date conversion capabilities, it serves as both an educational tool and a functional application. 
