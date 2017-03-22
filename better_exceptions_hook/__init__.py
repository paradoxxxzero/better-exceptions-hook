def hook():
    try:
        import better_exceptions
    except Exception:
        print("Can't hook better_exceptions.")
