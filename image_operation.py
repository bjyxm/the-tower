def compare(im1, im2, box):
    # 1. Crop Image
    im1_crop = im1.crop(box)
    im2_crop = im2.crop(box)

    # 2. Calc Histogram
    hist1 = im1_crop.histogram()
    hist2 = im2_crop.histogram()
    r1, g1, b1 = hist1[:256], hist1[256:512], hist1[512:]
    r2, g2, b2 = hist2[:256], hist2[256:512], hist2[512:]

    # 3. Convert to weighted histogram
    r1 = _weighted_histogram(r1)
    g1 = _weighted_histogram(g1)
    b1 = _weighted_histogram(b1)
    r2 = _weighted_histogram(r2)
    g2 = _weighted_histogram(g2)
    b2 = _weighted_histogram(b2)

    # 4. Compare Histograms
    diff = 0
    for pair in zip(r1+g1+b1, r2+g2+b2):
        diff += abs(pair[0] - pair[1])

    # 5. Normalize & Return
    box_width = box[2] - box[0]
    box_height = box[3] - box[1]
    return diff / (box_width * box_height)


def _weighted_histogram(hist_of_one_channel):
    num_of_bins = len(hist_of_one_channel) // 8 + 1
    shared_hist = [0] * num_of_bins
    for v, count in enumerate(hist_of_one_channel):
        for h in range(0, 32):
            if h * 8 <= v < (h + 1) * 8:
                shared_hist[h] += (h + 1 - v / 8) * count
                shared_hist[h + 1] += (v / 8 - h) * count
                break
    return shared_hist
