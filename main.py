from numpy import tan, deg2rad, linspace
import matplotlib.pyplot as plt


# METERS FROM THE GROUND
MFTG = 25

# AVERAGE PIXELS PER METERS
APPM = 1067
APPM = APPM/2


def area_from_fov(fov: float):
    return 2*MFTG*tan(deg2rad(fov/2))


def required_pixels_from_fov(fov: float):
    return APPM*area_from_fov(fov) 


def get_APPM(fov: float, pixel_count: int):
    return pixel_count/area_from_fov(fov)


def get_info(fov: float):
    print(f"Area viewed from FOV {fov}:", area_from_fov(fov))
    print(f"Camera resolution required to get {APPM} px/m at FOV {fov}:", required_pixels_from_fov(fov))
    


if __name__ == "__main__":
    print("4K camera vertical:", get_APPM(47, 2160))
    print("4K camera horizontal: ", get_APPM(100, 3840))
    min_fov = 10
    max_fov = 70
    x = linspace(min_fov, max_fov, max_fov - min_fov + 1)
    y = required_pixels_from_fov(x)
    print(type(y))

    fig, axs = plt.subplots()
    axs.plot(x, y)
    axs.set_yscale('log')
    # axs.axis('equal')
    # axs.set(xlim=(min_fov, max_fov), ylim=(y[0], y[0]+50))
    plt.show()



