#  Copyright 2022 Joshua Brown
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import keithley_dmm as kdmm

# import keithley_dmm_constants as dmmconst

mydmm = kdmm.KeithleyDmm()
# mysmu = KeiSmu.KeithleySeries2400InteractiveSmu()

mydmm.initialize("USB0::0x05E6::0x2460::04312353::INSTR")

print(mydmm.instrument_id_query())

# -- Reset the instrument to the default settings.
# reset()
# -- Set the measure function to DC voltage.
# dmm.measure.func = dmm.FUNC_DC_VOLTAGE
# -- Set the measurement range to 10 V.
# dmm.measure.range = 10
# -- Set the number of power line cycles to 10.
# dmm.measure.nplc = 10
# -- Set the input impedance to auto so it selects 10 Gohm for the 10 V range.
# dmm.measure.inputimpedance = dmm.IMPEDANCE_AUTO
# -- Enable autozero.
# dmm.measure.autozero.enable = dmm.ON
# -- Set the averaging filter type to repeating.
# dmm.measure.filter.type = dmm.FILTER_REPEAT_AVG
# -- Set filter count to 100.
# dmm.measure.filter.count = 100
# -- Enable the filter.
# dmm.measure.filter.enable = dmm.ON
# -- Read the voltage value.
# print(dmm.measure.read())


mydmm.close()
