def plot_cuboid(center, size):
    """
       Create a data array for cuboid plotting.


       ============= ================================================
       Argument      Description
       ============= ================================================
       center        center of the cuboid, triple
       size          size of the cuboid, triple, (x_length,y_width,z_height)
       :type size: tuple, numpy.array, list
       :param size: size of the cuboid, triple, (x_length,y_width,z_height)
       :type center: tuple, numpy.array, list
       :param center: center of the cuboid, triple, (x,y,z)
   """
    # suppose axis direction: x: to left; y: to inside; z: to upper
    # get the (left, outside, bottom) point
    import numpy as np
    ox, oy, oz = center
    l, w, h = size

    x = np.linspace(ox-l/2,ox+l/2,num=5)  #Return evenly spaced numbers over a specified interval
    y = np.linspace(oy-w/2,oy+w/2,num=5)
    z = np.linspace(oz-h/2,oz+h/2,num=5)
    x1, z1 = np.meshgrid(x, z)
    y11 = np.ones_like(x1)*(oy-w/2)
    y12 = np.ones_like(x1)*(oy+w/2)
    x2, y2 = np.meshgrid(x, y)
    z21 = np.ones_like(x2)*(oz-h/2)
    z22 = np.ones_like(x2)*(oz+h/2)
    y3, z3 = np.meshgrid(y, z)
    x31 = np.ones_like(y3)*(ox-l/2)
    x32 = np.ones_like(y3)*(ox+l/2)

    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # outside surface
    ax.plot_wireframe(x1, y11, z1, color='r', rstride=1, cstride=1, alpha=0.6)
    # inside surface
    ax.plot_wireframe(x1, y12, z1, color='y', rstride=1, cstride=1, alpha=0.6)
    # bottom surface
    ax.plot_wireframe(x2, y2, z21, color='g', rstride=1, cstride=1, alpha=0.6)
    # upper surface
    ax.plot_wireframe(x2, y2, z22, color='b', rstride=1, cstride=1, alpha=0.6)
    # left surface
    ax.plot_wireframe(x31, y3, z3, color='c', rstride=1, cstride=1, alpha=0.6)
    # right surface
    ax.plot_wireframe(x32, y3, z3, color='m', rstride=1, cstride=1, alpha=0.6)
    ax.set_xlabel('X')
    ax.set_xlim(-100, 100)
    ax.set_ylabel('Y')
    ax.set_ylim(-100, 100)
    ax.set_zlabel('Z')
    ax.set_zlim(-100, 100)
    plt.show()



def test():
    center = [0, 0, 0]
    length = 32 * 2
    width = 50 * 2
    height = 100 * 2
    plot_cuboid(center, (length, width, height))


if __name__ == '__main__':
    test()