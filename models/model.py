from .SEmodel import Model as semodel

# Mode Factory that maps modes to classes
Arch_FACTORY = {
    "none": semodel,
}

def get_arch(mode, *args, **kwargs):
    """Fetch the appropriate PointNet model based on the mode."""
    if mode not in Arch_FACTORY:
        raise ValueError(f"Mode {mode} is not available.")
    return Arch_FACTORY[mode](*args, **kwargs)
