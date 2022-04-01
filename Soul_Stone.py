# ==================== #
# Soul Stone           #
# Nat Cagle 2022-04-01 #
# ==================== #
# Description:

import arcpy
from arcpy import AddMessage as write

#            ___________________________________
#           | Thanos did nothing wrong. The     |
#           | data has been deficient for the   |
#           | past 3 years. It is geometrically |
#           | degenerate. I am it's gardener.   |
#      _    /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
#   __(.)< ‾
#~~~\___)~~~



TDS = arcpy.GetParameterAsText(0)
arcpy.env.workspace = TDS
arcpy.env.overwriteOutput = True
featureclass = arcpy.ListFeatureClasses()
featureclass.sort()
total = 0
snap_total = 0

write("\n\nIt's a simple calculus. This computer is finite, its resources finite.\nIf data is left unchecked, data will cease to exist.")
write("Fun isn't something one considers when balancing a database.\nBut this... does put a smile on my face.\n")
for fc in featureclass:
	fc_count = int(arcpy.GetCount_management(fc).getOutput(0))
	if fc_count == 0:
		continue
	total += fc_count
	count = 0
	with arcpy.da.UpdateCursor(fc, 'OID@') as ucursor:
		for urow in ucursor:
			count +=1
			if (count % 2) == 0:
				ucursor.deleteRow()
	snap_count = int(count/2)
	write("Snapped {0} out of {1} features in {2}.".format(snap_count, fc_count, fc))
	write("{0} is perfectly balanced, as all things should be.".format(fc))
	snap_total += snap_count
write("\n{0} out of {1} total features snapped.\n".format(snap_total, total))
write("You were going home late, scrounging for RAM. Your computer was on the brink of collapse.\nI'm the one who stopped that. You know what's happened since then?\nThe databases born have known nothing but fast connections and clean features.\nIt's a paradise.")
write("I finally rest. And watch the sun rise on a grateful database.\nThe hardest choices require the strongest wills.\n\n")
