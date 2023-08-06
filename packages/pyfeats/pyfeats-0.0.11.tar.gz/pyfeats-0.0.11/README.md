# Image Feature Extraction in Region-of-Interest
A collection of python functions for feature extraction. The features are calculated inside a Region of Interest (ROI) and not for the whole image: the image is actually a polygon.

## 1. Features

### 1.1 Textural Features
1. First Order Statistics/Statistical Features (FOS/SF)
2. Gray Level Co-occurence Matrix (GLCM/SGLDM)
3. Gray Level Difference Statistics (GLDS)
4. Neighborhood Gray Tone Difference Matrix (NGTDM)
5. Statistical Feature Matrix (SFM)
6. Law's Texture Energy Measures (LTE/TEM)
7. Fractal Dimension Texture Analysis (FDTA)
8. Gray Level Run Length Matrix (GLRLM)
9. Fourier Power Spectrum (FPS)
10. Shape Parameters
11. Gray Level Size Zone Matrix (GLSZM)
12. Higher Order Spectra (HOS)
13. Local Binary Pattern (LPB)

### 1.2 Morphological Features
1. Grayscale Morphological Analysis
2. Multilevel Binary Morphological Analysis

### 1.3 Histogram Based Features
1. Histogram
2. Multi-region histogram
3. Correlogram

### 1.4 Multi-scale Features
1. Fractal Dimension Texture Analysis (FDTA)
2. Amplitude Modulation – Frequency Modulation (AM-FM)
3. Discrete Wavelet Transform (DWT)
4. Stationary Wavelet Transform (SWT)
5. Wavelet Packets (WP)
6. Gabor Transform (GT)

### 1.5 Other Features
1. Zernikes’ Moments
2. Hu’s Moments
3. Threshold Adjacency Matrix (TAS)
4. Histogram of Oriented Gradients (HOG)

## 2. Use
Download pyfeats using
```console
pip install pyfeats
```

Import pyfeats using
```cpython
import pyfeats
```


## 3. How to use each feature set
For the following sections, assume
* _f_ is a grayscale image as a numpy ndarray, 
* _mask_ is an image as a numpy ndarray but with 2 values: 0 (zero) and 1 (one) with 1 indicating the ROI, where the features shall be calculated (values outside ROI are ignored),
* _perimeter_ is like _mask_ but indicates the perimeter of the ROI. 

### 3.1 Textural Features
#### 3.1.1 First Order Statistics/Statistical Features (FOS/SF)
```python
features, labels = fos(f, mask)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.

    Returns
    -------
    features : numpy ndarray
        Feature set as defined in theory.
    labels : list
        Labels of features.
    '''
```
#### 3.1.2 Gray Level Co-occurence Matrix (GLCM/SGLDM)
```python
features_mean, features_range, labels_mean, labels_range = glcm_features(f, ignore_zeros)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    ignore_zeros : int, optional
        Ignore zeros in image f. The default is True.

    Returns
    -------
    features_mean : numpy ndarray
        Haralick's features, mean
    features_range : numpy ndarray
        Haralick's features, same as before but range
    labels_mean : list
        Labels of features_mean.
    labels_range: list
        Labels of features_range.
    '''
```
#### 3.1.3 Gray Level Difference Statistics (GLDS)
```python
features, labels = glds_features(f, mask, Dx, Dy)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else.
    Dx : int, optional
        Array with X-coordinates of vectors denoting orientation. The default
        is [0,1,1,1].
    Dy : int, optional
        Array with Y-coordinates of vectors denoting orientation. The default
        is [1,1,0,-1].
        
    Returns
    -------
    features : numpy ndarray
        Feature set as defined in theory.
    labels : list
        Labels of features.
    '''
```
#### 3.1.4 Neighborhood Gray Tone Difference Matrix (NGTDM)
```python
features, labels = ngtdm_features(f, mask, d)
    '''  
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    d : int, optional
        Distance for NGTDM. Default is 1.

    Returns
    -------
    features : numpy ndarray
        Feature set as defined in theory.
    labels : list
        Labels of features.
    '''
```
#### 3.1.5 Statistical Feature Matrix (SFM)
```python
features, labels = sfm_features(f, mask, Lr, Lc)
    '''  
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    Lr : int, optional
        Parameters of SFM. The default is 4.
    Lc : int, optional
        Parameters of SFM. The default is 4.

    Returns
    -------
    features : numpy ndarray
        Feature set as defined in theory.
    labels : list
        Labels of features.
    '''
```
#### 3.1.6 Law's Texture Energy Measures (LTE/TEM)
```python
features, labels = lte_measures(f, mask, l)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    l : int, optional
        Law's mask size. The default is 7.

    Returns
    -------
    features : numpy ndarray
        Feature set as defined in theory.
    labels : list
        Labels of features.
    '''
```
#### 3.1.7 Fractal Dimension Texture Analysis (FDTA)
```python
h, labels = fdta(f, mask, s)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    s : int, optional
        max resolution to calculate Hurst coefficients. The default is 3

    Returns
    -------
    h : numpy ndarray
        Hurst coefficients.
    labels : list
        Labels of h.
    '''
```
#### 3.1.8 Gray Level Run Length Matrix (GLRLM)
```python
features, labels = glrlm_features(f, mask, Ng)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    Ng : int, optional
        Image number of gray values. The default is 256.

    Returns
    -------
    features : numpy ndarray
        Feature set as defined in theory.
    labels : list
        Labels of features.
    '''
```
#### 3.1.9 Fourier Power Spectrum (FPS)
```python
features, labels = fps(f, mask)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.

    Returns
    -------
    features : numpy ndarray
        Feature set as defined in theory.
    labels : list
        Labels of features.
    '''
```
#### 3.1.10 Shape Parameters
```python
features, labels = shape_parameters(f, mask, perimeter, pixels_per_mm2)
    ''' 
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    perimeter : numpy ndarray
         Image N1 x N2 with 1 if pixels belongs to perimeter of ROI, 0 else.
    pixels_per_mm2 : int, optional
        Density of image f. The default is 1.

    Returns
    -------
    features : numpy ndarray
        Feature set as defined in theory.
    labels : list
        Labels of features.
    '''
```
#### 3.1.11 Gray Level Size Zone Matrix (GLSZM)
```python
features, labels = glszm_features(f, mask)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else.

    Returns
    -------
    features : numpy ndarray
        Feature set as defined in theory.
    labels : list
        Labels of features.
    '''
```
#### 3.1.12 Higher Order Spectra (HOS)
```python
features, labels = hos_features(f, th)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    th : list, optional
        Angle to calculate Radon Transform. The default is [135,140].

    Returns
    -------
    features : numpy ndarray
        Entropy of bispectrum of radeon transform of image for each angle in theta.
    labels : list
        Labels of features.
    '''
```
#### 3.1.13 Local Binary Pattern (LPB)
```python
features, labels = lbp_features(f, mask, P, R)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    P : list, optional
        Number of points in neighborhood. The default is [8,16,24].
    R : list, optional
        Radius/Radii. The default is [1,2,3].

    Returns
    -------
    features : numpy ndarray
        Energy and entropy of LBP image (2 x 1).
    labels : list
        Labels of features.
    '''
```

### 3.2 Morphological Features
#### 3.2.1 Gray-scale Morphological Analysis
```python
pdf, cdf = grayscale_morphology_features(f, N)
    ''' 
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    N : np.array, optional
        Maximum number of scales. The default is 30.

    Returns
    -------
    pdf : numpy ndarray
        Probability density function (pdf) of pattern spectrum.
    cdf : numpy ndarray
        Cumulative density function (cdf) of pattern spectrum.
    '''
```
#### 3.2.2 Multilevel Binary Morphological Analysis
```python
pdf_L, pdf_M, pdf_H, cdf_L, cdf_M, cdf_H = multilevel_binary_morphology_features(img, mask, N, thresholds):
    ''' 
    Parameters
    ----------
    img : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    N : np.array, optional
        Maximum number of scales. The default is 30.
    thresholds: list, optional
        Thresholds to get the 3 binary images. The default is [25, 50].

    Returns
    -------
    pdf_L : numpy ndarray
        Probability density function (pdf) of pattern spectrum for image L.
    pdf_M : numpy ndarray
        Probability density function (pdf) of pattern spectrum for image M.
    pdf_H : numpy ndarray
        Probability density function (pdf) of pattern spectrum for image H.
    cdf_L : numpy ndarray
        Cumulative density function (cdf) of pattern spectrum for image L.
    cdf_M : numpy ndarray
        Cumulative density function (cdf) of pattern spectrum for image M.
    cdf_H : numpy ndarray
        Cumulative density function (cdf) of pattern spectrum for image H.
    '''   
```

### 3.3 Histogram Based Features
#### 3.3.1 Histogram
```python
H, labels = histogram(f, mask, bins)
    ''' 
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    bins : int, optional
         Bins for histogram. The default is 32.


    Returns
    -------
    H : numpy ndarray
        Histogram of image f for 256 gray levels.
    labels : list
        Labels of features, which are the bins' number.
    '''
```
#### 3.3.2 Multi-region histogram
```python
features, labels = multiregion_histogram(f, mask, bins, num_eros, square_size)
    ''' 
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    bins : int, optional
        Bins for histogram. Default is 32.
    num_eros : int, optional
        Times of erosion to be performed. Default is 3.
    square_size : int, optional
        Kernel where erosion is performed, here a squared. Default square's
        size is 3.
        
    Returns
    -------
    features : numpy ndarray
        Histogram of f and f after erosions as a vector e.g. [32 x num_eros].
    labels : list
        Labels of features.
    '''
```
#### 3.3.3 Correlogram
```python
Hd, Ht, labels = correlogram(f, mask, bins_digitize, bins_hist, flatten)
    ''' 
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    bins_digitize : int, optional
         Number of bins for discrete distances and thetas. The default is 32.
    bins_hist : int, optional
        Number of bins for histogram. The default is 32.
    flatten : bool, optional
        Return correlogram as 1d array if True or 2d array if False. The 
        default is False.

    Returns
    -------
    Hd : numpy ndarray
        Correlogram for distance.
    Ht : numpy ndarray
        Correlogram for angles.
    labels : list
        Labels of features.
    '''
```

### 3.4 Multi-scale Features
#### 3.4.1 Fractal Dimension Texture Analysis (FDTA)
```python
h, labels = fdta(f, mask, s)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    s : int, optional
        max resolution to calculate Hurst coefficients. The default is 3

    Returns
    -------
    h : numpy ndarray
        Hurst coefficients.
    labels : list
        Labels of h.
    '''
```
#### 3.4.2 Amplitude Modulation – Frequency Modulation (AM-FM)
```python
features, labels = amfm_features(f, bins)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    bins: int, optional
        Bins for the calculated histogram. The default is 32.

    Returns
    -------
    features : numpy ndarray
        Histogram of IA, IP, IFx, IFy as a concatenated vector.
    labels : list
        Labels of features.
    '''
```
#### 3.4.3 Discrete Wavelet Transform (DWT)
```python
features, labels = dwt_features(f, mask, wavelet, levels)
    ''' 
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    wavelet : str, optional
         Filter to be used. Check pywt for filter families. The default is 'bior3.3'
    levels : int, optional
        Levels of decomposition. Default is 3.

    Returns
    -------
    features : numpy ndarray
        Mean and std of each detail image. Appromimation images are ignored.
    labels : list
        Labels of features.
    '''
```
#### 3.4.4 Stationary Wavelet Transform (SWT)
```python
features, labels = swt_features(f, mask, wavelet, levels)
    ''' 
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    wavelet : str, optional
         Filter to be used. Check pywt for filter families. The default is 'bior3.3'
    levels : int, optional
        Levels of decomposition. Default is 3.

    Returns
    -------
    features : numpy ndarray
        Mean and std of each detail image. Appromimation images are ignored.
    labels : list
        Labels of features.
    '''
```
#### 3.4.5 Wavelet Packets (WP)
```python
features, labels = wp_features(f, mask, wavelet, maxlevel) 
    ''' 
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    wavelet : str, optional
         Filter to be used. Check pywt for filter families. The default is 'cof1'
    maxlevel : int, optional
        Levels of decomposition. Default is 3.

    Returns
    -------
    features : numpy ndarray
        Mean and std of each detail image. Appromimation images are ignored.
    labels : list
        Labels of features.
    '''
```
#### 3.4.6 Gabor Transform (GT)
```python
features, labels = gt_features(f, mask, deg, freq)
    ''' 
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    mask : numpy ndarray
        Mask image N1 x N2 with 1 if pixels belongs to ROI, 0 else. Give None
        if you want to consider ROI the whole image.
    deg: int, optinal
        Quantized degrees. The default is 4 (0, 45, 90, 135 degrees)
    freq: list, optional
        frequency of the gabor kernel. The default is [0.05, 0.4]

    Returns
    -------
    features : numpy ndarray
        Mean and std for the resulted image: (f o gabor_filter)(x,y)
        
    labels : list
        Labels of features.
    '''  
```

### 3.5 Other Features
#### 3.5.1 Zernikes’ Moments
```python
features, labels = zernikes_moments(f, radius)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    radius : int, optional
        Radius to calculate Zernikes moments. The default is 9.

    Returns
    -------
    features : numpy ndarray
        Zernikes' moments.
    labels : list
        Labels of features.
    '''
```
#### 3.5.2 Hu’s Moments
```python
features, labels = hu_moments(f)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.

    Returns
    -------
    features : numpy ndarray
        Hu's moments.
    labels : list
        Labels of features.
    '''
```
#### 3.5.3 Threshold Adjacency Matrix (TAS)
```python
features, labels = tas_features(f)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.

    Returns
    -------
    features : numpy ndarray
        Feature values.
    labels : list
        Labels of features.
    '''  
```
#### 3.5.4 Histogram of Oriented Gradients (HOG)
```python
fd, labels = hog_features(f, ppc, cpb)
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    ppc : int, optional
        Pixels per cell. The default is 8.
    cpb : int, optional
        Cells per block. The default is 3.

    Returns
    -------
    fd : numpy ndarray
        Histogram of Oriented Gradients flattened.
    labels : list
        Labels of features.
    '''
```
