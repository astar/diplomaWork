from astrogrid import acr, DSA, MySpace
acr.login()

db = DSA('ivo://uk.ac.cam.ast/iphas-dsa-catalog/IDR')
app = db.query('Select Top 100 * From PhotoObjBest', saveAs = '#test.vot')
url = app.results()[0]
m = MySpace()
m.readfile(url,ofile='test.vot')
