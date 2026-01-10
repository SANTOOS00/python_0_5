















class GardenManager:
    def 




























# ft_garden_analytics.py

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    # 1️⃣ إنشاء مدير الحدائق
    manager = GardenManager()

    # 2️⃣ إضافة حدائق
    manager.add_garden("Alice")
    manager.add_garden("Bob")

    # 3️⃣ إضافة نباتات لكل حديقة
    manager.add_plant_to_garden("Alice", OakTree())
    manager.add_plant_to_garden("Alice", Rose())
    manager.add_plant_to_garden("Alice", Sunflower())
    
    manager.add_plant_to_garden("Bob", Tulip())
    manager.add_plant_to_garden("Bob", Daisy())

    # 4️⃣ تنمية النباتات
    print("All gardens are helping their plants grow...")
    manager.grow_all_gardens()

    # 5️⃣ عرض التقارير النهائية
    print("=== Garden Reports ===")
    manager.show_reports()

    # 6️⃣ مثال على استخدام دوال الكلاس أو الثابتة
    print(f"Total gardens managed: {GardenManager.total_gardens()}")
