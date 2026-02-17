"""
Presentation Validation Script
Checks all required files for Vehicle Analysis presentation
"""

import os
from pathlib import Path

def validate_presentation_files():
    """Validate all required files for the presentation"""
    
    current_dir = Path.cwd()
    print(f"Checking files in: {current_dir}")
    print("="*60)
    
    # Required files for presentation
    required_files = {
        "PowerPoint Presentation": "Vehicle_Delivery_Analysis_Data_Science_Presentation.pptx",
        "Interactive Heatmap": "05_store_delivery_heatmap.html",
        "Presentation Guide": "Presentation_Guide.md",
        "Source Notebook": "Vehicle_Analysis_Technical_Demo.ipynb"
    }
    
    # Visualization files (embedded in PowerPoint)
    visualization_files = [
        "01_vehicle_delivery_time_overview.png",
        "02a_vehicle_weather_boxplot.png", 
        "02b_vehicle_weather_bar.png",
        "03a_vehicle_traffic_boxplot.png",
        "03b_vehicle_traffic_bar.png", 
        "04a_combined_conditions_heatmap.png",
        "04b_vehicle_efficiency_rankings.png"
    ]
    
    print("📋 PRESENTATION FILES STATUS")
    print("-" * 40)
    
    all_good = True
    
    # Check required files
    for description, filename in required_files.items():
        if os.path.exists(filename):
            file_size = os.path.getsize(filename) / 1024  # KB
            print(f"✅ {description}: {filename} ({file_size:.1f} KB)")
        else:
            print(f"❌ {description}: {filename} - NOT FOUND")
            all_good = False
    
    print(f"\n📊 VISUALIZATION FILES (Embedded in PowerPoint)")
    print("-" * 50)
    
    # Check visualization files
    missing_viz = []
    for viz_file in visualization_files:
        if os.path.exists(viz_file):
            print(f"✅ {viz_file}")
        else:
            print(f"❌ {viz_file} - NOT FOUND")
            missing_viz.append(viz_file)
            all_good = False
    
    print(f"\n🎯 PRESENTATION SUMMARY")
    print("-" * 30)
    print(f"📁 Working Directory: {current_dir}")
    print(f"🎨 Static Visualizations: {len(visualization_files) - len(missing_viz)}/{len(visualization_files)} available")
    print(f"🌐 Interactive Elements: {'✅ Ready' if os.path.exists('05_store_delivery_heatmap.html') else '❌ Missing'}")
    print(f"📊 Main Presentation: {'✅ Ready' if os.path.exists('Vehicle_Delivery_Analysis_Data_Science_Presentation.pptx') else '❌ Missing'}")
    
    if all_good:
        print(f"\n🎉 ALL FILES READY FOR PRESENTATION!")
        print(f"📋 Next Steps:")
        print(f"   1. Open: Vehicle_Delivery_Analysis_Data_Science_Presentation.pptx")
        print(f"   2. Read: Presentation_Guide.md for presentation tips")
        print(f"   3. Test: 05_store_delivery_heatmap.html in browser")
        print(f"   4. Practice: Alt+Tab transitions for live demo")
    else:
        print(f"\n⚠️  Some files are missing. Check the issues above.")
    
    print(f"\n📚 ACADEMIC PRESENTATION DETAILS")
    print("-" * 40)
    print(f"🎯 Target Audience: Data Science Students & Instructor")
    print(f"⏱️  Recommended Duration: 15-20 minutes + Q&A")
    print(f"🔬 Focus: Methodology and Technical Approaches")
    print(f"📖 Slides: 13 total (Title → Analysis → Findings → Discussion)")
    print(f"🎪 Interactive Demo: Slide 9 (Geospatial Visualization)")
    
    return all_good

if __name__ == "__main__":
    validate_presentation_files()