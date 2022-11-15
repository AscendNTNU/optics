#https://confluence.ascendntnu.no/display/PER/Cameras
from numpy import tan, deg2rad, linspace
import matplotlib.pyplot as plt


# METERS FROM THE GROUND
MFTG = 25

# AVERAGE PIXELS PER METERS
APPM = 1067


def area_from_fov(fov: float):
    return 2*MFTG*tan(deg2rad(fov/2))


def required_pixels_from_fov(fov: float):
    return APPM*area_from_fov(fov)


def get_APPM(fov: float, pixel_count: int):
    return pixel_count/area_from_fov(fov)


def get_info(hfov: float, vfov: float, hpixels: int, vpixels: int, name: str):
    print()
    print(name)
    print()
    print(f"Given the HORIZONTAL {hfov} and horizontal pixel count {hpixels}:")
    print(f"    APPM: {get_APPM(hfov, hpixels)}")
    print(f"    Area: {area_from_fov(hfov)}")
    print()
    print(f"Given the VERTICAL {vfov} and horizontal pixel count {vpixels}:")
    print(f"    APPM: {get_APPM(vfov, vpixels)}")
    print(f"    Area: {area_from_fov(vfov)}")
    print()
    print(name)
    print()

    # print(f"Area viewed from FOV {fov}:", area_from_fov(fov))
    # print(f"Camera resolution required to get {APPM} px/m at FOV {fov}:", required_pixels_from_fov(fov))


if __name__ == "__main__":

    hfov = 12.1
    vfov = 10.5
    hpixels = 5328
    vpixles = 4608
    get_info(hfov, vfov, hpixels, vpixles, "Allied")

    hfov = 12.4
    vfov = 8.3
    hpixels = 5472
    vpixles = 3648
    get_info(hfov, vfov, hpixels, vpixles, "Flir")

    hfov = 11.2
    vfov = 8.4
    hpixels = 4912
    vpixles = 3684
    get_info(hfov, vfov, hpixels, vpixles, "E-con")



    # old
    # fig, axs = plt.subplots()
    # axs.plot(x, y)
    # axs.set_yscale('log')
    # # axs.axis('equal')
    # # axs.set(xlim=(min_fov, max_fov), ylim=(y[0], y[0]+50))
    # plt.show()
    # old



