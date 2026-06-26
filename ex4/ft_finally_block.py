#! /usr/bin/env python3
class GardenError(Exception):
    def __init__(self, msg: str = "Unknown garden error") -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown garden error") -> None:
        super().__init__(msg)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: list) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    valid_list = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(valid_list)

    print("\nTesting invalid plants...")
    invalid_list = ["Tomato", "lettuce"]
    test_watering_system(invalid_list)
    print("\nCleanup always happens, even with errors!")
