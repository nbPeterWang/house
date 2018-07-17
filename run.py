from flask import Flask, render_template, request
from flask import jsonify
from pc2 import test
from pred1 import P1
from pred2 import P2
from pred3 import P3
import outcsx
import clean

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

#获取数据
@app.route('/getdata')
def getdata():
    test.get_house()
    return str(test.num)

#导出数据
@app.route('/exportdata')
def exportdata():
    outcsx.outdata()
    return "导出数据成功"
#加工数据
@app.route('/cleandata')
def cleandata():
    clean.cleanData()
    return "加工数据成功"
#处理各个表单事件
@app.route('/myform1',methods=['GET', 'POST'])
def pred1d():
    b=request.values.get("a")
    c=P1.predict1(float(b))
    return str(c)
@app.route('/myform2',methods=['GET', 'POST'])
def pred2d():
    b1=request.values.get("b")
    c1=P2.predict2(float(b1))
    return str(c1)
@app.route('/myform3',methods=['GET', 'POST'])
def pred3d():
    b2=request.values.get("c")
    d2=request.values.get("d")
    c2=P3.predict3(b2,d2)
    return str(c2)

if __name__ == '__main__':
    app.run()
