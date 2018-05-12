from pie_chart import PieChart
from pie_arc import PieArc


arcs = [PieArc('one'), PieArc('two'), PieArc('three'), PieArc('four')]

pie = PieChart(arcs)

pie.draw()
