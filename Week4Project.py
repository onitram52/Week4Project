class ROICalculator:
    def __init__(self):
        self.investment = float(input("Please enter your initial investment (in dollars): "))
        self.return_ = float(input("please enter your return on investment (in dollars): "))
        self.maintenance_costs = float(input("Please enter your maintenance costs (in dollars): "))
        
    def calculate_roi(self):
        roi_ = (self.return_ - self.investment - self.maintenance_costs)/ self.investment * 100
        if roi_ > 0:
            return (f"Your ROI is: {roi_}%. nice...")
        else:
            return (f"Your ROI is: {roi_}%. lol...")

    def calculate_profit(self):
        profit = self.return_ - self.investment - self.maintenance_costs
        if profit > 0:
            return (f"Your profit is: ${profit}. Wow, you must have worked hard for that!")
        else:
            return (f"Your profit is: ${profit}. Glory to the proletariat!")

    def calculate_payback_period(self):
        profit = self.return_ - self.investment - self.maintenance_costs
        payback_period = self.investment / float(abs(profit))
        return (f"Your payback period will be {payback_period} months")
        
roi_calc = ROICalculator()

print(roi_calc.calculate_roi())
print(roi_calc.calculate_profit())
print(roi_calc.calculate_payback_period())
