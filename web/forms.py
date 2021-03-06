# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    BooleanField,
    PasswordField,
    TextAreaField,
    SubmitField,
    IntegerField,
)
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


# 注册表单
class SignUpForm(FlaskForm):
    user_name = StringField(
        "user name",
        validators=[
            DataRequired(message="用户名不能为空"),
            Length(5, 15, message="用户名在5-15个字之间"),
            Regexp("^[A-Za-z][A-Za-z0-9_.]*$", message="用户名只能由字母数字和下划线组成"),
        ],
    )
    user_email = StringField(
        "user email",
        validators=[
            Email(message="邮箱格式错误"),
            DataRequired(message="邮箱不能为空"),
            Length(max=128),
        ],
    )
    password = PasswordField("Password", validators=[DataRequired(message="必须填写密码")])
    confim_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(message="用户名不能为空"),
            EqualTo("password", message="两次密码不一致"),
        ],
    )
    submit = SubmitField("register")


class LoginForm(FlaskForm):
    user_name = StringField(
        "user name",
        validators=[
            DataRequired(message="用户名不能为空"),
            Length(5, 15, message="用户名在5-15个字之间"),
        ],
    )
    remember_me = BooleanField("remember me", default=False)
    password = PasswordField("Password", validators=[DataRequired(message="必须填写密码")])
    submit = SubmitField("log in")


class AboutMeForm(FlaskForm):
    describe = TextAreaField("about me", validators=[DataRequired(), Length(max=140)])
    submit = SubmitField("YES!")


class AddMonitorItemForm(FlaskForm):
    commodityName = StringField("Commodity name", validators=[DataRequired()])
    hopePrice = IntegerField("Hope price", validators=[DataRequired()])
    submit = SubmitField("Add monitor")


class UserinformationChangeForm(FlaskForm):
    username = StringField(
        "用户名(登录使用)",
        validators=[
            DataRequired(),
            Regexp("^[A-Za-z][A-Za-z0-9_.]*$", message="用户名只能由字母数字和下划线组成"),
        ],
    )
    name = StringField("真实姓名")
    birthDay = StringField("出生日期")
    telephone = StringField("电话号码",validators=[Regexp("[0-9]+",message="电话号码必须是纯数字")])
    Email = StringField(
        "Email", validators=[DataRequired(message="用户名不能为空"), Email(message="邮箱格式不正确")]
    )
    # old_password = PasswordField("旧密码", validators=[DataRequired(message="密码不能为空")])
    # password = PasswordField("新密码", validators=[DataRequired(message="密码不能为空")])
    # confirm_password = PasswordField(
    #     "确认新密码",
    #     validators=[DataRequired("不能为空"), EqualTo("password", message="两次密码不一致")],
    # )
    submit = SubmitField("保存")

class PasswordForm(FlaskForm):
    old_pass = PasswordField("旧密码", validators=[DataRequired(message="旧密码不能为空")])
    new_pass = PasswordField("新密码", validators=[DataRequired(message="请填写新密码"),Regexp("^(?![0-9]+$)(?![a-z]+$)(?![A-Z]+$)(?!([^(0-9a-zA-Z)])+$).{6,20}$",message="密码至少包含数字、字母字符中的两种以上")])
    confirm_pass = PasswordField("确认新密码", validators=[DataRequired(message="请重新输入新密码"),EqualTo("new_pass", message="两次密码不一致")])
    submit = SubmitField("保存")
