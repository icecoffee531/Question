from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse


class AuthMD(MiddlewareMixin):  # 验证登录
    white_list = ['/apis/login/', '/apis/regist/']  # 白名单
    black_list = ['/black/', ]  # 黑名单
    ret = {'status': 0, 'url': '', 'msg': ''}   # 默认状态

    def process_request(self, request):     # 请求之前
        request_url = request.path_info     # 获取请求路径
        # 黑名单的网址限制访问
        if request_url in self.black_list:
            self.ret['msg'] = "这是非法请求"
            self.ret['url'] = '/'
        # 白名单的网址或者登陆用户不做限制
        # 判断是否在白名单内或者已经有了session(表示已经登录了)
        elif request_url in self.white_list or request.session.get("uid"):
            return None
        else:
            self.ret['msg'] = "请登录后,再访问!"
            self.ret['url'] = "/"
        return JsonResponse(self.ret)