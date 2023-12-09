from utils.casedata_yaml import yaml_data


class AssertCheck:

    def assert_check(self, data, respon):
        for assert_data in data:
            for type, chack_data in assert_data.items():
                real_data = yaml_data.get_jsonpath(respon, list(chack_data)[0])
                expect_data = list(chack_data)[1]
                if type in ["contains","cons"]:
                    self.contains_data(real_data, expect_data)
                elif type in ["len"]:
                    self.len_data(real_data, expect_data)
                elif type in ["equal"]:
                    self.equal_data(real_data, expect_data)



    def contains_data(self, data, expr):
        assert expr in data, "断言：%s 包含 %s 出错" % (expr, data)

    def len_data(self, data, expr):
        assert len(data) == expr, "断言：%s 的长度与 %s 对比出错" % (data, expr)

    def equal_data(self, data, expr):
        assert str(expr) == str(data), "断言：%s 等于 %s 出错" % (expr, data)

assert_check = AssertCheck()

if __name__ == '__main__':
    data = [{"contains": "[$.token,'ey']"}]
    res = {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMzA1NjYsInVzZXJuYW1lIjoiMTM0ODgwMTAwMDIiLCJleHAiOjE3MDI2MjMwMjIsImVtYWlsIjpudWxsfQ.eSeY8pKAqRRxu5mFQDycOLdYND0_I2kurUb-EImXypI"
    }
    assert_check.assert_check([{"contains": "[$.token,'ey']"}], res)
