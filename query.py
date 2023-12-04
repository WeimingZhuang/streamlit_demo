import pandas as pd
from datetime import datetime, timedelta

class Query:

    def __init__(self):

        self.current_date = datetime.today().strftime('%Y-%m-%d')
        self.df = self.generate_new_data(pd.read_excel('History_data.xlsx'))
        self.map_location = ["市中心", "唐人街", "接力塔", "贫民窟", "联合大厦", "林荫大道", "地铁", "医院", "隔离中心"]
        self.game_mode = ["鳄龟", "雪犁", "枪手", "15Min", "人群"]

    def generate_new_data(self, df):
        start_date = df.iloc[-1, 0]
        one_month_later = datetime.today() + timedelta(days=30)
        if start_date < one_month_later:
            new_df = {'时间': [], '组合': []}

            # 生成100个时间点，每个时间点间隔8小时
            for i in range(100):
                start_date += timedelta(hours=8)
                new_df['时间'].append(start_date)
                new_df['组合'].append(df.iloc[i, 1])

            new_df = pd.concat([df, pd.DataFrame(new_df)], ignore_index=True)
            new_df.to_excel('History_data.xlsx', index=False)
            return new_df
        else:
            return df

    def base_data(self, df):
        # 将Date设置为index
        df.set_index('Date', inplace=True)

        df_dic = df.to_dict(orient='index')

        data = []
        count = 0

        for day, row in df_dic.items():
            for time, value in row.items():
                if value == '联合大厦鳄龟':
                    count += 1
                    if count == 4:
                        break  # 结束内部循环
                if count != 0:
                    data.append({'时间': datetime.combine(day, time), '组合': value})

            if count == 4:
                break  # 结束外部循环
        result = pd.DataFrame(data)
        return result
    
    def query1(self, date1):
        if date1 > self.current_date:
            # 返回从今天到date1的日期列表
            date_list = pd.date_range(start=self.current_date, end=date1, freq='D').strftime('%Y-%m-%d').tolist()
        elif date1 < self.current_date:
            # 返回从date1到今天的日期列表
            date_list = pd.date_range(start=date1, end=self.current_date, freq='D').strftime('%Y-%m-%d').tolist()
        else:
            date_list = [date1]
        # 筛选出date_list中的数据
        result1 = self.df[self.df['时间'].dt.strftime('%Y-%m-%d').isin(date_list)].reset_index(drop=True)
        return result1
    def query3(self, date3):
        if date3 > self.current_date:
            # 返回从今天到date1的日期列表
            date_list = pd.date_range(start=self.current_date, end=date3, freq='D').strftime('%Y-%m-%d').tolist()
        elif date3 < self.current_date:
            # 返回从date1到今天的日期列表
            date_list = pd.date_range(start=date3, end=self.current_date, freq='D').strftime('%Y-%m-%d').tolist()
        else:
            date_list = [date3]
        # 筛选出date_list中的数据
        result1 = self.df[self.df['时间'].dt.strftime('%Y-%m-%d').isin(date_list)].reset_index(drop=True)
        return result1
    def query4(self, date4):
        if date4 > self.current_date:
            # 返回从今天到date1的日期列表
            date_list = pd.date_range(start=self.current_date, end=date4, freq='D').strftime('%Y-%m-%d').tolist()
        elif date4 < self.current_date:
            # 返回从date1到今天的日期列表
            date_list = pd.date_range(start=date4, end=self.current_date, freq='D').strftime('%Y-%m-%d').tolist()
        else:
            date_list = [date4]
        # 筛选出date_list中的数据
        result4 = self.df[self.df['时间'].dt.strftime('%Y-%m-%d').isin(date_list)].reset_index(drop=True)
        return result4
    def query5(self, date5):
        if date5 > self.current_date:
            # 返回从今天到date1的日期列表
            date_list = pd.date_range(start=self.current_date, end=date5, freq='D').strftime('%Y-%m-%d').tolist()
        elif date5 < self.current_date:
            # 返回从date1到今天的日期列表
            date_list = pd.date_range(start=date5, end=self.current_date, freq='D').strftime('%Y-%m-%d').tolist()
        else:
            date_list = [date5]
        # 筛选出date_list中的数据
        result5 = self.df[self.df['时间'].dt.strftime('%Y-%m-%d').isin(date_list)].reset_index(drop=True)
        return result5
    def query6(self, date6):
        if date6 > self.current_date:
            # 返回从今天到date1的日期列表
            date_list = pd.date_range(start=self.current_date, end=date6, freq='D').strftime('%Y-%m-%d').tolist()
        elif date6 < self.current_date:
            # 返回从date1到今天的日期列表
            date_list = pd.date_range(start=date6, end=self.current_date, freq='D').strftime('%Y-%m-%d').tolist()
        else:
            date_list = [date6]
        # 筛选出date_list中的数据
        result6 = self.df[self.df['时间'].dt.strftime('%Y-%m-%d').isin(date_list)].reset_index(drop=True)
        return result6
    def query7(self, date7):
        if date7 > self.current_date:
            # 返回从今天到date1的日期列表
            date_list = pd.date_range(start=self.current_date, end=date7, freq='D').strftime('%Y-%m-%d').tolist()
        elif date7 < self.current_date:
            # 返回从date1到今天的日期列表
            date_list = pd.date_range(start=date7, end=self.current_date, freq='D').strftime('%Y-%m-%d').tolist()
        else:
            date_list = [date7]
        # 筛选出date_list中的数据
        result7 = self.df[self.df['时间'].dt.strftime('%Y-%m-%d').isin(date_list)].reset_index(drop=True)
        return result7
    def query8(self, date8):
        date_list = pd.date_range(start=self.current_date, end=date8, freq='D').strftime('%Y-%m-%d').tolist()
        # 筛选出date_list中的数据
        result8 = self.df[self.df['时间'].dt.strftime('%Y-%m-%d').isin(date_list)].reset_index(drop=True)
        return result8
    def query2(self, map_location, game_mode, date2):
        text = map_location + game_mode
        if text not in self.df['组合'].tolist():
            result2 = '没有该玩法'
        else:
            if date2 > self.current_date:
                # 返回从今天到date1的日期列表
                date_list = pd.date_range(start=self.current_date, end=date2, freq='D').strftime('%Y-%m-%d').tolist()
            elif date2 < self.current_date:
                # 返回从date1到今天的日期列表
                date_list = pd.date_range(start=date2, end=self.current_date, freq='D').strftime('%Y-%m-%d').tolist()
            else:
                date_list = [date2]
            # 根据text和date_list筛选出数据
            result2 = self.df[(self.df['组合'] == text) & (self.df['时间'].dt.strftime('%Y-%m-%d').isin(date_list))].reset_index(drop=True)
        return result2


if __name__ == '__main__':
    query = Query()
    # result1 = query.query1('2023-09-01')
    # result2 = query.query2('联合大厦', '鳄鱼', '2023-09-01')
    print(query.base_data(pd.read_excel('ATF突变体.xlsx')))