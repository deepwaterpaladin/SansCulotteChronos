from datetime import datetime, timedelta
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

# Initialize Rich console
console = Console()
REVOLUTIONARY_START_DATE = datetime(1792, 9, 22)
REVOLUTIONARY_MONTHS = [
    "Vendémiaire", "Brumaire", "Frimaire", "Nivôse", "Pluviôse", "Ventôse",
    "Germinal", "Floréal", "Prairial", "Messidor", "Thermidor", "Fructidor", "Sans-culottides"
]


def gregorian_to_revolutionary(date):
    """Convert a Gregorian date to the French Revolutionary Calendar."""
    delta_days = (date - REVOLUTIONARY_START_DATE).days
    if delta_days < 0:
        return "Date is before the French Revolutionary Calendar was established."

    year = delta_days // 365 + 1
    day_of_year = delta_days % 365

    if day_of_year >= 360:
        return year, "Sans-culottides", day_of_year - 359

    month = day_of_year // 30
    day = day_of_year % 30 + 1

    return year, REVOLUTIONARY_MONTHS[month], day


def revolutionary_to_gregorian(year, month, day):
    """Convert a French Revolutionary Calendar date to Gregorian."""
    if month == "Sans-culottides":
        day_of_year = 360 + day - 1
    else:
        try:
            month_index = REVOLUTIONARY_MONTHS.index(month)
        except ValueError:
            return "Invalid month name."
        day_of_year = month_index * 30 + day - 1

    delta_days = (year - 1) * 365 + day_of_year
    return REVOLUTIONARY_START_DATE + timedelta(days=delta_days)


def display_menu():
    """Display the main menu."""
    console.print(
        "[bold cyan]French Revolutionary Calendar Converter[/bold cyan]", justify="center")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Option")
    table.add_column("Description")
    table.add_row("1", "Get today's date on the Revolutionary Calendar")
    table.add_row(
        "2", "Convert a past Gregorian date to the Revolutionary Calendar")
    table.add_row(
        "3", "Convert a Revolutionary date to the Gregorian Calendar")
    table.add_row("4", "Exit")
    console.print(table)


def main():
    while True:
        display_menu()
        choice = Prompt.ask("[bold green]Choose an option[/bold green]",
                            choices=["1", "2", "3", "4"], default="1")

        if choice == "1":
            today = datetime.today()
            year, month, day = gregorian_to_revolutionary(today)
            console.print(
                f"Today on the Revolutionary Calendar: Year {year}, Month {month}, Day {day}")
            cont = Prompt.ask("Do you wish to continue?")
            if cont == "no" or cont == "No":
                break
            else:
                console.clear()
        elif choice == "2":
            date_str = Prompt.ask("Enter a Gregorian date (YYYY-MM-DD)")
            try:
                gregorian_date = datetime.strptime(date_str, "%Y-%m-%d")
                year, month, day = gregorian_to_revolutionary(gregorian_date)
                console.print(
                    f"Revolutionary Date: Year {year}, Month {month}, Day {day}")
            except ValueError:
                console.print(
                    "Invalid date format. Please use YYYY-MM-DD.", style="bold red")
            cont = Prompt.ask("Do you wish to continue? (Yes/No)")
            if cont == "no" or cont == "No":
                break
            else:
                console.clear()
        elif choice == "3":
            year = int(Prompt.ask("Enter the Revolutionary year"))
            month = Prompt.ask("Enter the Revolutionary month")
            day = int(Prompt.ask("Enter the Revolutionary day"))
            result = revolutionary_to_gregorian(year, month, day)
            if isinstance(result, str):
                console.print(result, style="bold red")
            else:
                console.print(f"Gregorian Date: {result.strftime('%Y-%m-%d')}")
            cont = Prompt.ask("Do you wish to continue?")
            if cont == "no" or cont == "No":
                break
            else:
                console.clear()
        elif choice == "4":
            console.print("[bold yellow]Goodbye![/bold yellow]",
                          justify="center")
            break


if __name__ == "__main__":
    main()
