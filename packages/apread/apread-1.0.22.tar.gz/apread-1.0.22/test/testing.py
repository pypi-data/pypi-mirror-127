from apread.apreader import APReader
import os

# find current directory
dirname = os.path.dirname(__file__)
file = os.path.join(dirname, 'Example_Catman_Data.bin')

outdir = os.path.join(dirname, 'output')

# create a reader
reader = APReader(file)

# plot every channel
#for channel in reader.Channels:
#    channel.plot('mat')

# plot every group
# for group in reader.Groups:
#     group.plot()

#reader.plot()

# save all entries as json
reader.save('json')

# # specify output directory
# reader.save('json', outdir)

# # equivalent to the one before
for channel in reader.Channels:
    print (channel.getas('json'))
for group in reader.Groups:
    print (group.getas('json'))
