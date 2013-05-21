'''
Created on May 21, 2013

@author: pshu
'''
import matplotlib.pyplot as plot
# from pylab import hist,plot

if __name__ == '__main__':
    f = open('hist.txt','r');
    reps = [];
    lines = [];
    while(True): 
        line = f.readline()
        if len(line)!=0:
            ln,repstr = line.split()[0:2]
            lines.append(int(ln))
            reps.append(int(repstr))
        else:
            break;
    
    line_rep = zip(reps,lines);
    
    middle_rep = 0.5*(max(reps)+min(reps))

    old_lines = sum([ p[1] for p in line_rep if p[0]< middle_rep])
    new_lines = sum([ p[1] for p in line_rep if p[0]>=middle_rep])
    total_line_num = sum(lines)
    
    print "old ratio", old_lines*1.0/total_line_num
    print "new ratio", new_lines*1.0/total_line_num
    
#     print line_rep
    
    
    print lines[0]*1.0/total_line_num
    
#     plot.bar(reps,lines)
#     plot.pie([ b/sum(lines) for b in lines])
#     plot.axis([-1,max(reps),0,max(lines)])
#     plot.show()
#     fig = plot.figure()
#     ax = fig.add_subplot(111)
#     
    