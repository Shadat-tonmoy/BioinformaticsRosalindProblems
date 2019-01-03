import operator


def spectrumConvolution(spectrum):
    spectrum.sort()
    l = len(spectrum)
    convo_dict = dict()

    for i in range(0, l - 1):
        for j in range(i + 1, l):
            d = spectrum[j] - spectrum[i]
            if d in convo_dict:
                convo_dict[d] += 1
            else:
                convo_dict[d] = 1
    sorted_convo_dict = sorted(convo_dict.items(), key=operator.itemgetter(1))
    return sorted_convo_dict[::-1]


def generateConvolution(spectrum):
    convolution_dict = dict()
    for i in range(1, len(spectrum)):
        for j in range(i):
            if spectrum[i] == spectrum[j]:
                continue

            diff = abs(spectrum[i] - spectrum[j])
            if diff in convolution_dict:
                convolution_dict[diff] += 1
            else:
                convolution_dict[diff] = 1

    sorted_convolutional_dict = sorted(convolution_dict.items(), key=operator.itemgetter(1))
    return sorted_convolutional_dict[::-1]


spectrum = '0 137 186 323'
spectrum = spectrum.split()
spectrum_list = [int(i) for i in spectrum]
convo_dict = generateConvolution(spectrum_list)
ans = ''
for k, v in convo_dict:
    for i in range(v):
        ans += str(k) + ' '

print(ans)