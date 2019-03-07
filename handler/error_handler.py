from app import app, jsonify, make_response

# '''
# 错误码处理入口
# '''
#
#
# @app.errorhandler(404)
# def not_found(error):
#     return make_response(
#         jsonify({'code': 404, 'error': 'Not find!', 'msg': str(error)}),
#         404
#     )