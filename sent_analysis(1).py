# replace multiple spaces into one space first
# perl -p -i".bak" -le 's/\s+/ /g' book.csv
# perl -p -i".bak" -le 's/\s+/ /g' proneg
# perl -p -i".bak" -le 's/\s*be\s+//g' proneg

import csv;
import sys;
import os;

def IsNotNull(value):
    return value is not None and len(value) > 0;
#enddef

###################################################################
# load dict
dicta = [];
dictb = [];
dictc = [];
dictd = [];

#################################################################
# remove multiple spaces in dict
# cmd = 'perl -p -i".bak" -le ' + "'s/\\s+/ /g' " + sys.argv[1];
# print cmd;
# os.system(cmd);
# 
# cmd = 'perl -p -i".bak" -le ' + "'s/\\s+/ /g' " + sys.argv[2];
# print cmd;
# os.system(cmd);
# 
# cmd = 'perl -p -i".bak" -le ' + "'s/\\s+/ /g' " + sys.argv[3];
# print cmd;
# os.system(cmd);

#################################################################
if (len(sys.argv) < 3) :
   fa = 'positive-words.txt';
   fb = 'negative-words.txt';
else :
   fa = sys.argv[2];
   fb = sys.argv[3];
# endif

# create dict (pro)
fd = open(fa, 'r');   
for line in fd:
   t = line.strip().lower();

   if (IsNotNull(t)) :
      dicta.append(t);
   # endif
# endfor
fd.close();

# create dict (neg)
fd = open(fb, 'r');   
for line in fd:
   t = line.strip().lower();

   if (IsNotNull(t)) :
      dictb.append(t);
   # endif
# endfor
fd.close();

#################################################################
# counting
with open('short_input.txt', 'rt') as csvfile:

   spamreader = csv.reader(csvfile, delimiter=',', quotechar='"');
   nline = 0;

   for row in spamreader:
      # if (len(row) < 10) :
      #   continue;
      # endif
      
      if (not IsNotNull(row)) :
         continue;
      # endif

      if (not IsNotNull(row[0])) :
         continue;
      # endif

      nline = nline + 1;
      if (nline == 1) :
         header = ["msgid"]; # row;

         header.append('poscnt');
         header.append('negcnt');
         header.append('netcnt');

         line = ','.join(header);
         print(line);

         continue;
      #endif

      #####################################
      # --> lowercase & split
      t = row[0].lower();

      qa = 0;
      qb = 0;

      for d in dicta :
         if (d in t) :
            qa = qa + 1;
            # print d;
            # print t;
         # endif
      # endfor

      for d in dictb :
         if (d in t) :
            qb = qb + 1;
         # endif
      # endfor

      qc = qa - qb;

      ################################################
      nrow = [str(nline-1), str(qa), str(qb), str(qc)];

      line = '';
      line = line + ','.join(nrow);

      # print(row[0]);
      print(t+'\t'+line);
   # endfor
# endwith
