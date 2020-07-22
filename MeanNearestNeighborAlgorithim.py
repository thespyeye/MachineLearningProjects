# This algorithim works by taking all of the training data, averaging all of the images into a single "mean" image,
# and then comparing that "mean" image to all of the testing image.

# Don't mind my eccentric variable names. They are just random things I came up with.

global checker
global prototesting
global globalimagelength
checker = [] # This program has a built in system to check its accuracy. This list is
             # whether a testing image is the same thing as the training images or if
             # it is not the same thing as the training images.
globalheh = 0 # How many testing images you have.
globalhehe = 0 # How many training images you have.
globalimagelength = 64 # How many 1's or 0's are in our image.
training = [] # Where all of your training images go.
prototesting = [] #Where all of your testing images go. (What the program is identifying as either similar to the 
                  # training images or not similar to the training images.)

def Nearneigh(tested, trained):
   # i = (len(trained))
    e = 0
    r = 0
    hahahaha = 0
    globalhehe
    protomean1 = []
    section = 0
    for hahahaha in range (globalhehe):
        
        e = 0
        i = (globalimagelength)
        section = hahahaha
        for e in range(i):
            r = section
            if r < 0:
                r = 0
            protomean1.append(trained[(e+(section*i))])
            ee = 0
            aa = []
            aah = []
            e += 1
            heeed = 0
            Yes = 0
            Yess = 0
            eeee = 0
        hahahaha += 1
        section += 1
    for ee in range (globalhehe):
        Yess = 0
        yyes = 0
        for heeed in range(i):
          aa.append(protomean1[heeed+(ee*i)])
          heeed += 1
    eeee = 0
    for eeee in range(i):
      yyes = 0
      Yes = 0
      Yess = 0
      for Yes in range (globalhehe):
        Yess = Yess + aa[(Yes*i)+eeee]
        Yes += 1
      yyes = Yess/len(aa)
      aah.append(yyes*i)
      eeee += 1
    ff = 0
    reeprotoprotoconfidence = 0
    reeprotoconfidence = []
    reeprotoconfidence2 = 0
    reeconfidence = 0
    for ff in range(i):
        reeprotoprotoconfidence = (aah[ff]*tested[ff])
        reeprotoconfidence.append(reeprotoprotoconfidence)
        ff = ff+1
    fff = 0
    yeess = (len(reeprotoconfidence)-1)
    reeprotoprotoconfidence = 0
    for fff in range (yeess):
        reeprotoprotoconfidence = reeprotoprotoconfidence + reeprotoconfidence[fff]
        fff = fff+1
    reeprotoconfidence2 = reeprotoprotoconfidence/(len(reeprotoconfidence))
    print(reeprotoconfidence2)
    
    if reeprotoconfidence2 >= 0.17:
        reeconfidence = 1
    else:
        reeconfidence = 0
    maainresults.append(reeconfidence)
    
def formatting():
   jimboo = 0
   global testeded
   testeded = []
   jimboo1 = 0
   jimbooo1 = 320
   for jimboo1 in range(jimbooo1):
      testeded.append(0)
      jimboo += 1


countser = 0
realaccuracy = 0
formatting()
global maainresults
maainresults = []
REE = 0
jar = 0
testeded1 = []
for REE in range(globalimagelength):
  testeded1.append(0)
  REE += 1

jarr = 0
jaaarrr = 0
jimmmmy = 0
a_nice_EE = 0

for countser in range(globalheh):
  jimmmmy = 0
  for jimmmmy in range(globalimagelength):
     testeded1[jimmmmy] = prototesting[((countser*globalimagelength)+jimmmmy)]
     jimmmmy += 1   
  Nearneigh(testeded1, training)
jar = 0
jarr = 0
jaaarrr = 0
countser = countser + 1
countserer = 0
countserer = 0
for countserer in range(globalheh):
    print(maainresults[countserer])
    
    if (maainresults[countserer] == checker[countserer]): # Delete this code if you dont have the answers for your testing
      jar += 1                                            # images.
    else:
      jar += 0
    countserer = countserer+1
jaaarrr = jar/(globalheh)
print(jaaarrr*100)