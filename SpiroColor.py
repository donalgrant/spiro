import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import colormaps

import numpy as np
import colorsys

def modify_colormap(cmap_name='turbo', saturation_factor=1.0, brightness_factor=1.0, contrast_factor=1.0):
  """
  Modifies the saturation, brightness, and contrast of a colormap.

  Args:
    cmap_name: The name of the colormap to modify.
    saturation_factor: A factor to multiply the saturation by.
    brightness_factor: A factor to multiply the value channel by (brightness).
    contrast_factor: A factor to adjust the contrast (1.0 is no change).

  Returns:
    A matplotlib colormap object with the modified colors.
  """

  cmap = plt.get_cmap(cmap_name)
  rgb_colors = cmap(np.linspace(0, 1, 256))[:, :3]

  hsv_colors = np.array([colorsys.rgb_to_hsv(*color) for color in rgb_colors])

  # Adjust saturation, brightness, and contrast
  hsv_colors[:, 1] *= saturation_factor
  hsv_colors[:, 2] *= brightness_factor
  hsv_colors[:, 2] = np.clip(hsv_colors[:, 2], 0, 1)  # Ensure value stays within [0, 1]
  hsv_colors[:, 2] = (hsv_colors[:, 2] - hsv_colors[:, 2].mean()) * contrast_factor + hsv_colors[:, 2].mean()
  hsv_colors[:, 2] = np.clip(hsv_colors[:, 2], 0, 1)  # Ensure value stays within [0, 1]

  rgb_colors = np.array([colorsys.hsv_to_rgb(*color) for color in hsv_colors])
  for j in range(3):
      rgb_colors[:, j] = np.clip(rgb_colors[:, j], 0, 1)  # Ensure value stays within [0, 1]

  new_cmap = plt.matplotlib.colors.ListedColormap(rgb_colors)
  return new_cmap

def modify_colormap_saturation(cmap_name, saturation_factor=1.0):
  """
  Modifies the saturation of a colormap.

  Args:
    cmap_name: The name of the colormap to modify.
    saturation_factor: A factor to multiply the saturation by.

  Returns:
    A matplotlib colormap object with the modified colors.
  """

  cmap = plt.get_cmap(cmap_name)
  rgb_colors = cmap(np.linspace(0, 1, 256))[:, :3]

  hsv_colors = np.array([colorsys.rgb_to_hsv(*color) for color in rgb_colors])
  hsv_colors[:, 1] *= saturation_factor  # Adjust saturation
  rgb_colors = np.array([colorsys.hsv_to_rgb(*color) for color in hsv_colors])

  new_cmap = plt.matplotlib.colors.ListedColormap(rgb_colors)
  return new_cmap

def morph_colormaps(cmap_name1, cmap_name2, fraction):
  """
  Morphs two matplotlib colormaps.

  Args:
    cmap1: The first colormap.
    cmap2: The second colormap.
    fraction: The fraction of the way to morph from cmap1 to cmap2.

  Returns:
    A new matplotlib colormap.
  """
  
  cmap1 = plt.get_cmap(cmap_name1)
  cmap2 = plt.get_cmap(cmap_name2)

  cmap1_colors = cmap1(np.linspace(0, 1, 256))[:, :3]
  cmap2_colors = cmap2(np.linspace(0, 1, 256))[:, :3]

  morph_colors = cmap1_colors * (1 - fraction) + cmap2_colors * fraction

  new_cmap = plt.matplotlib.colors.ListedColormap(morph_colors)
  return new_cmap

def cmap_from_list(clist,cname=None):
    if cname is None:
        cname=''
        for c in clist: cname+=c[:2]
    cmap=LinearSegmentedColormap.from_list(cname,clist)
    mpl.colormaps.register(cmap=cmap)
    return cmap

cmap1 = cmap_from_list(["Red","Orange","hotpink"],'cmap1')
cmap2 = cmap_from_list(["rebeccapurple","darkmagenta","orchid","pink"],'cmap2')
cmap3 = cmap_from_list(["seagreen","teal","cornflowerblue","mediumblue","indigo"],'cmap3')

clist = [ 'xkcd:'+i for i in ['dark peach','peach','light peach','pale peach'] ]
peaches = cmap_from_list(clist,'peaches')

cyans = cmap_from_list(["xkcd:dark aqua","xkcd:dark cyan","xkcd:cyan","xkcd:light cyan","xkcd:ice"],'cyans')

clist = [ 'xkcd:'+i for i in ['sapphire','vibrant blue','carolina blue','navy blue','azul','sapphire'] ]
pretty_blues = cmap_from_list(clist,'pretty_blues')

clist = [ 'xkcd:'+i for i in ['blood red','raw umber','light forest green','forest green'] ]
wreath = cmap_from_list(clist,'wreath')

clist = [ 'xkcd:'+i for i in ['dark gold','gold','dark gold','muddy green','dark gold'] ]
gold = cmap_from_list(clist,'gold')

clist = [ 'xkcd:'+i for i in ['kelly green','light green','vivid green','grass green'] ]
emerald_woman= cmap_from_list(clist,'emerald_woman')

clist = [ 'xkcd:'+i for i in ['carnation pink','baby pink','lipstick red','darkish pink','powder pink'] ]
pinks = cmap_from_list(clist,'pinks')

clist = [ 'xkcd:'+i for i in ['lavender pink','pale mauve','pinky purple','purpleish','lavender pink'] ]
pale_pink = cmap_from_list(clist,'pale_pink')

clist = [ 'xkcd:'+i for i in ['red','crimson','fire engine red','dull red','carnation',
                              'lipstick red','bright red','blood red','red'] ]
pretty_reds = cmap_from_list(clist,'pretty_reds')

def cmap_list():
    return ['pretty_blues','wreath','gold','emerald_woman','pinks','pale_pink',
            'cmap1','cmap2','cmap3','cyans',
            'viridis','magma','inferno','plasma','cividis',
            'spring','summer','winter','autumn','Wistia','cool',
            'hot','gist_heat','copper',
            'Dark2','tab10','tab20','tab20b','Set1','Set2','Set3',
            'Pastel1','Pastel2','Paired','Accent',
            'ocean','terrain','gist_earth','gist_stern','prism',
            'turbo','gnuplot','brg','gist_rainbow','rainbow','jet',
            'nipy_spectral','gist_ncar',
            'bone','twilight','twilight_shifted','hsv',
            'Greys','Purples','Blues','Greens','Oranges','Reds','YlOrBr',
            'YlOrRd','OrRd','PuRd','RdPu','BuPu','GnBu','PuBu',
            'YlGnBu','PuBuGn','BuGn','YlGn'
            ]

def apply_dither(c,dfactor):
    if dfactor==0: return c
    spread = max(c)-min(c)
    g = np.random.standard_normal(len(c))*spread*dfactor
    return c+g

all_cmaps = list(colormaps)

def random_cmap():
    return all_cmaps[ np.random.randint(len(all_cmaps)) ]
