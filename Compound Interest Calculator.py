import tkinter as tk
from tkinter import ttk
import datetime

def calculate_monthly_compound_interest(initial_principal, monthly_rate, goal, bonus_times_per_year, bonus_amount, start_month, bonus_months):
    current_principal = initial_principal
    total_interest = 0
    now = datetime.datetime.now()
    year = now.year
    months = 0
    months_d = start_month
    total_bonus = 0
    history = []

    while current_principal < goal:
        interest = current_principal * monthly_rate
        total_interest += interest
        current_principal += interest
        months += 1
        months_d += 1

        if months_d in bonus_months:
            current_principal += bonus_amount
            total_bonus += bonus_amount

        if months_d == 13:
            months_d = 1
            year += 1

        history.append({
            "year": year,
            "month_need": months,
            "month": months_d,
            "principal": initial_principal if months == 1 else previous_total_amount,
            "interest": interest,
            "total_interest": total_interest,
            "bonus_amount": total_bonus,
            "total_amount": current_principal
        })

        previous_total_amount = current_principal

    return history

def on_calculate():
    initial_principal = float(entry_initial_principal.get())
    annual_rate = float(entry_annual_rate.get())
    monthly_rate = annual_rate / 12
    goal = float(entry_goal.get())
    bonus_times_per_year = int(entry_bonus_times_per_year.get())
    bonus_amount = float(entry_bonus_amount.get())
    start_month = int(entry_start_month.get())
    bonus_months = list(map(int, entry_bonus_months.get().split()))

    history = calculate_monthly_compound_interest(initial_principal, monthly_rate, goal, bonus_times_per_year, bonus_amount, start_month, bonus_months)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"{labels['Year']:^6} {labels['Month']:^6} {labels['Principal']:^14} {labels['Interest']:^12} {labels['Total Interest']:^16} {labels['Bonus Amount']:^14} {labels['Total Amount']:^14}\n")
    for record in history:
        result_text.insert(tk.END, f"{record['year']:^6} {record['month']:^6} {record['principal']:^14,.2f} {record['interest']:^12,.2f} {record['total_interest']:^16,.2f} {record['bonus_amount']:^14,.2f} {record['total_amount']:^14,.2f}\n")

    months_needed = record['month_need']
    years_needed = months_needed // 12
    remaining_months = months_needed % 12
    if years_needed > 0 and remaining_months > 0:
        result_text.insert(tk.END, f"\n{labels['Goal Time (Months)']}: {record['month_need']} {labels['months']}\n")
        result_text.insert(tk.END, f"{labels['Goal Time (Years)']}: {years_needed} {labels['years']}{remaining_months} {labels['months']}\n")
    elif years_needed == 0:
        result_text.insert(tk.END, f"\n{labels['Goal Time (Months)']}: {remaining_months} {labels['months']}\n")
    else:
        result_text.insert(tk.END, f"\n{labels['Goal Time (Years)']}: {years_needed} {labels['years']}\n")

def change_language(event):
    global labels
    lang = lang_var.get()
    labels = translations[lang]
    update_labels()

def update_labels():
    lbl_initial_principal.config(text=labels['Initial Principal'])
    lbl_annual_rate.config(text=labels['Annual Rate'])
    lbl_goal.config(text=labels['Goal'])
    lbl_bonus_times_per_year.config(text=labels['Bonus Times Per Year'])
    lbl_bonus_amount.config(text=labels['Bonus Amount'])
    lbl_start_month.config(text=labels['Start Month'])
    lbl_bonus_months.config(text=labels['Bonus Months'])
    button_calculate.config(text=labels['Calculate'])

translations = {
    'English': {
        'Initial Principal': 'Initial Principal',
        'Annual Rate': 'Annual Rate (e.g., 0.20 for 20%)',
        'Goal': 'Goal',
        'Bonus Times Per Year': 'Bonus Times Per Year',
        'Bonus Amount': 'Bonus Amount',
        'Start Month': 'Start Month (1-12)',
        'Bonus Months': 'Bonus Months (separated by space)',
        'Calculate': 'Calculate',
        'Year': 'Year',
        'Month': 'Month',
        'Principal': 'Principal',
        'Interest': 'Interest',
        'Total Interest': 'Total Interest',
        'Bonus Amount': 'Bonus Amount',
        'Total Amount': 'Total Amount',
        'Goal Time (Months)': 'Goal Time (Months)',
        'Goal Time (Years)': 'Goal Time (Years)',
        'months': 'months',
        'years': 'years'
    },
    '中文': {
        'Initial Principal': '初始本金',
        'Annual Rate': '年化利率 (例如：0.20 代表 20%)',
        'Goal': '目标金额',
        'Bonus Times Per Year': '每年奖金发放次数',
        'Bonus Amount': '每次奖金发放金额',
        'Start Month': '开始月份 (1-12)',
        'Bonus Months': '奖金发放月份 (用空格分隔)',
        'Calculate': '计算',
        'Year': '年',
        'Month': '月',
        'Principal': '本金',
        'Interest': '利息',
        'Total Interest': '累计利息',
        'Bonus Amount': '奖金金额',
        'Total Amount': '总金额',
        'Goal Time (Months)': '达到目标所需月数',
        'Goal Time (Years)': '达到目标所需年数',
        'months': '个月',
        'years': '年'
    },
    '日本語': {
        'Initial Principal': '初期元本',
        'Annual Rate': '年利率 (例: 0.20 は 20%)',
        'Goal': '目標金額',
        'Bonus Times Per Year': '年間ボーナス回数',
        'Bonus Amount': 'ボーナス金額',
        'Start Month': '開始月 (1-12)',
        'Bonus Months': 'ボーナス月 (スペースで区切る)',
        'Calculate': '計算',
        'Year': '年',
        'Month': '月',
        'Principal': '元本',
        'Interest': '利息',
        'Total Interest': '総利息',
        'Bonus Amount': 'ボーナス金額',
        'Total Amount': '総額',
        'Goal Time (Months)': '目標到達時間（月数）',
        'Goal Time (Years)': '目標到達時間（年数）',
        'months': 'ヶ月',
        'years': '年'
    }
}

# 默认语言
labels = translations['English']

# 创建主窗口
root = tk.Tk()
root.title("复利计算器")

# 语言选择
lang_var = tk.StringVar(value='English')
lang_menu = ttk.OptionMenu(root, lang_var, 'English', 'English', '中文', '日本語', command=change_language)
lang_menu.grid(column=0, row=0, columnspan=2)

# 创建输入框和标签
lbl_initial_principal = ttk.Label(root, text=labels['Initial Principal'])
lbl_initial_principal.grid(column=0, row=1)
entry_initial_principal = ttk.Entry(root)
entry_initial_principal.grid(column=1, row=1)

lbl_annual_rate = ttk.Label(root, text=labels['Annual Rate'])
lbl_annual_rate.grid(column=0, row=2)
entry_annual_rate = ttk.Entry(root)
entry_annual_rate.grid(column=1, row=2)

lbl_goal = ttk.Label(root, text=labels['Goal'])
lbl_goal.grid(column=0, row=3)
entry_goal = ttk.Entry(root)
entry_goal.grid(column=1, row=3)

lbl_bonus_times_per_year = ttk.Label(root, text=labels['Bonus Times Per Year'])
lbl_bonus_times_per_year.grid(column=0, row=4)
entry_bonus_times_per_year = ttk.Entry(root)
entry_bonus_times_per_year.grid(column=1, row=4)

lbl_bonus_amount = ttk.Label(root, text=labels['Bonus Amount'])
lbl_bonus_amount.grid(column=0, row=5)
entry_bonus_amount = ttk.Entry(root)
entry_bonus_amount.grid(column=1, row=5)

lbl_start_month = ttk.Label(root, text=labels['Start Month'])
lbl_start_month.grid(column=0, row=6)
entry_start_month = ttk.Entry(root)
entry_start_month.grid(column=1, row=6)

lbl_bonus_months = ttk.Label(root, text=labels['Bonus Months'])
lbl_bonus_months.grid(column=0, row=7)
entry_bonus_months = ttk.Entry(root)
entry_bonus_months.grid(column=1, row=7)

# 计算按钮
button_calculate = ttk.Button(root, text="Calculate", command=on_calculate)
button_calculate.grid(column=0, row=7, columnspan=2)

# 结果显示框
result_text = tk.Text(root, height=24, width=100)
result_text.grid(column=0, row=8, columnspan=2)

# 启动主循环
root.mainloop()

将每列数值和标题文字居中对齐