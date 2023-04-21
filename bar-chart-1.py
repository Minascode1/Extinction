import os
import matplotlib.pyplot as plt

h = '/Users/minakabki/Desktop/Dissertation-work'
h1 = '/Users/minakabki/Desktop/Dissertation-work/Het1Logfile/REvoSim_output'
h2 = '/Users/minakabki/Desktop/Dissertation-work/Het2Logfile/REvoSim_output'
h3 = '/Users/minakabki/Desktop/Dissertation-work/Het3Logfile/REvoSim_output'
h4 = '/Users/minakabki/Desktop/Dissertation-work/Het4Logfile/REvoSim_output'
h5 = '/Users/minakabki/Desktop/Dissertation-work/Het5Logfile/REvoSim_output'

nh = '/Users/minakabki/Desktop/Dissertation-work'
nh1 = '/Users/minakabki/Desktop/Dissertation-work/NonHet1Logfile/REvoSim_output'
nh2 = '/Users/minakabki/Desktop/Dissertation-work/NonHet2Logfile/REvoSim_output'
nh3 = '/Users/minakabki/Desktop/Dissertation-work/NonHet3Logfile/REvoSim_output'
nh4 = '/Users/minakabki/Desktop/Dissertation-work/NonHet4Logfile/REvoSim_output'
nh5 = '/Users/minakabki/Desktop/Dissertation-work/NonHet5Logfile/REvoSim_output'

parentDirectory = {
    'Heterogeneous': [h1, h2, h3, h4, h5],
    'Non-Heterogeneous': [nh1, nh2, nh3, nh4, nh5],
}

result = {
    'Heterogeneous': [],
    'Non-Heterogeneous': [],
}

for eachDir in parentDirectory:
    currentDir = parentDirectory[eachDir]

    for child in currentDir:
        childDir = os.fsencode(child)

        for file in os.listdir(childDir):
            myfile = file.decode('utf-8')

            if 'end' not in myfile and myfile.endswith('.txt'):
                with open(child + '/' + myfile, encoding='utf8') as f:
                    shouldGetNumberOfLivingDigitalOrganisms = False
                    for line in f:
                        line = line.strip()

                        if line.startswith("[I]"):
                            eachIteratioNumber = line.split(' ')[1]
                            if eachIteratioNumber == '7999':
                                shouldGetNumberOfLivingDigitalOrganisms = True
                            else:
                                shouldGetNumberOfLivingDigitalOrganisms = False
                        elif line.startswith("[P]"):
                            if shouldGetNumberOfLivingDigitalOrganisms == True:
                                try:
                                    # print('aaaaaaaaaaa', line)
                                    eachPopulationGridData = line.split(' ')[1]
                                    NumberOfLivingDigitalOrganisms = eachPopulationGridData.split(',')[4]
                                    result[eachDir].append(int(NumberOfLivingDigitalOrganisms))
                                except Exception as e:
                                    print('error', e)
                                    print('line',line.split(' '))

hetAvg = sum(result['Heterogeneous']) / len(result['Heterogeneous'])
nonHetAvg = sum(result['Non-Heterogeneous']) / len(result['Non-Heterogeneous'])

data = list((hetAvg, nonHetAvg))
labels = ['Heterogeneous', 'Non-Heterogeneous']

# Plot bar chart with combined data
plt.bar(labels, data, color=['purple', 'purple'], width=0.3)
plt.title('Impact of Mass Extinction on Species Richness in Heterogeneous and Non-Heterogeneous Environments')
plt.xlabel('Environment')
plt.ylabel('Number of Species ')
plt.show()