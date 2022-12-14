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


import comms_tools as comms
import keithley_dmm_constants as kconst
import keithley_dmm_measure_configuration as measure_config


class KeithleyDmm:
    """
    Placeholder docstring
    """
    def __init__(self):
        self.echocommand = 0
        self.node = 1
        self.resource_mgr = None
        self.resource_id = ""
        self.family = None
        # self.instrument_object = None
        self.instrumentcomms = comms.Communications()
        # self.buffer = buffer_config.Buffer()
        # self.dataqueue = dataqueue_config.DataQueueConfiguration()
        # self.display = display_config.DisplayConfiguration()
        # self.eventlog = eventlog_config.EventLogConfiguration()
        # self.localnode = localnode_config.LocalNodeConfiguration()
        # self.source = source_config.SourceConfiguration()
        self.measure = measure_config.MeasureConfiguration()
        # self.trigger = trigger_config.TriggerConfiguration()
        # self.tsplink = tsplink_config.TspLinkConfiguration()

    class InstrumentConnection(object):
        """
        Placeholder docstring description.
        """
        def __init__(self):
            self.resourcerm = None

    def initialize(self, instrument_resource_string, *args):
        """
        Placeholder docstring descriptions.
        """
        try:
            self.instrumentcomms.initialize(instrument_resource_string, *args)
            # self.buffer.mycomms = self.instrumentcomms
            # self.dataqueue._mycomms = self.instrumentcomms
            # self.display._mycomms = self.instrumentcomms
            # self.eventlog._mycomms = self.instrumentcomms
            # self.localnode._mycomms = self.instrumentcomms
            # self.source._mycomms = self.instrumentcomms
            self.measure._mycomms = self.instrumentcomms
            # self.trigger._mycomms = self.instrumentcomms
            # self.tsplink._mycomms = self.instrumentcomms
            # self.source.update_comms()
            self.measure.update_comms()
            # self.trigger.update_comms()
            # self.display.update_comms()
            # self.tsplink.update_comms()
        except:
            print("error")

    def reset(self):
        """
        This function resets commands to their default settings and clears the\
            buffers.
        :return: None
        """
        self.instrumentcomms.write("reset()")

    def instrument_id_query(self):
        """
        Placeholder docsting description.
        """
        return self.instrumentcomms.query("*IDN?")

    def close(self):
        """
        Placeholder docstring description.
        """
        self.instrumentcomms.close()
        return

    def available(self, functionality):
        """
        This function checks for the presence of specific instrument \
            functionality.

        :param functionality:
        :return:
        """
        self.instrumentcomms.write(f"presence = available({functionality})")

    def beep(self, duration, frequency):
        """
        This method generates an audible tone.

        :param frequency:
        :param duration:
        :return:
        """
        self.instrumentcomms.write(f"beeper.beep({duration},{frequency})")

    def delay(self, seconds):
        """
        This function delays the execution of the commands that follow it.

        :param seconds: (float) The number of seconds to delay (0 to 100 ks)
        :return: None
        """
        self.instrumentcomms.write(f"delay({seconds})")

    @property
    def terminals(self):
        """
        This attribute describes which set of input and output terminals the \
            instrument is using

        :return: Either 0 (TERMINALS_FRONT) or 1 (TERMINALS_REAR)
        """
        term = None
        self.instrumentcomms.write("terminals = smu.terminals")
        if "FRONT" in self.instrumentcomms.query("print(terminals)").rstrip():
            term = kconst.TERMINALS_FRONT
        else:
            term = kconst.TERMINALS_REAR
        return term

    @terminals.setter
    def terminals(self, terminals):
        """
        This attribute describes which set of input and output terminals the \
            instrument is using

        :param terminals: Either 0 (TERMINALS_FRONT) or 1 (TERMINALS_REAR)
        :return: None
        """
        if terminals == smuconst.TERMINALS_FRONT:
            self.instrumentcomms.write("smu.terminals=smu.TERMINALS_FRONT")
        else:
            self.instrumentcomms.write("smu.terminals=smu.TERMINALS_REAR")

    def waitcomplete(self):
        """
        This function waits for all previously started overlapped commands to \
            complete.

        :return: None
        """
        self.instrumentcomms.write("waitcomplete()")

    def get_buffer_reading_count(self, buffer_name="defbuffer1"):
        """
        This function returns the number of readings presently stored in the \
            specified reading buffer. If no reading
        buffer is specified, the default is defbuffer1.

        :param buffer_name: The reading buffer whose reading count will be \
            returned.
        :return:
        """
        return int(self.instrumentcomms.query(f"print({buffer_name}.n)").
                   rstrip())

    def get_buffer_value(self, buffer_name, index,
                         readings=False,
                         relativetimestamps=False,
                         formattedreadings=False,
                         fractionalseconds=False,
                         extravalues=False,
                         extravalueunits=False,
                         extraformattedvalues=False,
                         dates=False, seconds=False,
                         sourceformattedvalues=False,
                         sourcestatuses=False,
                         sourceunits=False,
                         statuses=False,
                         times=False,
                         timestamps=False,
                         units=False):
        """
        This function is used to return any one of the table values as part of\
            an instrument buffer at the specified index position.

        :param buffer_name:
        :param index:
        :param readings:
        :param relativetimestamps:
        :param formattedreadings:
        :param fractionalseconds:
        :param extravalues:
        :param extravalueunits:
        :param extraformattedvalues:
        :param dates:
        :param seconds:
        :param sourceformattedvalues:
        :param sourcestatuses:
        :param sourceunits:
        :param statuses:
        :param times:
        :param timestamps:
        :param units:
        :return: Any one of the table values as part of an instrument buffer.
        """
        write_string = "print("

        if readings:
            write_string += f"{buffer_name}.readings[{index}]"
        elif relativetimestamps:
            write_string += f"{buffer_name}.relativetimestamps[{index}]"
        elif formattedreadings:
            write_string += f"{buffer_name}.fractionalseconds[{index}]"
        elif fractionalseconds:
            write_string += f"{buffer_name}.fractionalseconds[{index}]"
        elif extravalues:
            write_string += f"{buffer_name}.extravalues[{index}]"
        elif extravalueunits:
            write_string += f"{buffer_name}.extravalueunits[{index}]"
        elif extraformattedvalues:
            write_string += f"{buffer_name}.extraformattedvalues[{index}]"
        elif dates:
            write_string += f"{buffer_name}.dates[{index}]"
        elif seconds:
            write_string += f"{buffer_name}.seconds[{index}]"
        elif sourceformattedvalues:
            write_string += f"{buffer_name}.sourceformattedvalues[{index}]"
        elif sourcestatuses:
            write_string += f"{buffer_name}.sourcestatuses[{index}]"
        elif sourceunits:
            write_string += f"{buffer_name}.sourceunits[{index}]"
        elif statuses:
            write_string += f"{buffer_name}.statuses[{index}]"
        elif times:
            write_string += f"{buffer_name}.times[{index}]"
        elif timestamps:
            write_string += f"{buffer_name}.timestamps[{index}]"
        elif units:
            write_string += f"{buffer_name}.units[{index}]"
        write_string += ")"
        return self.instrumentcomms.query(write_string).rstrip()
