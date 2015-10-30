# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""
Template file used by the OPF Experiment Generator to generate the actual
description.py file by replacing $XXXXXXXX tokens with desired values.

This description.py file was generated by:
'/Users/manpreet.singh/.pyenv/versions/venv/lib/python2.7/site-packages/nupic-0.3.5.dev0-py2.7.egg/nupic/swarming/exp_generator/ExpGenerator.pyc'
"""

from nupic.frameworks.opf.expdescriptionapi import ExperimentDescriptionAPI

from nupic.frameworks.opf.expdescriptionhelpers import (
  updateConfigFromSubConfig,
  applyValueGettersToContainer
  )

from nupic.frameworks.opf.clamodelcallbacks import *
from nupic.frameworks.opf.metrics import MetricSpec
from nupic.swarming.hypersearch.experimentutils import (InferenceType,
                                                        InferenceElement)
from nupic.support import aggregationDivide

from nupic.frameworks.opf.opftaskdriver import (
                                            IterationPhaseSpecLearnOnly,
                                            IterationPhaseSpecInferOnly,
                                            IterationPhaseSpecLearnAndInfer)


# Model Configuration Dictionary:
#
# Define the model parameters and adjust for any modifications if imported
# from a sub-experiment.
#
# These fields might be modified by a sub-experiment; this dict is passed
# between the sub-experiment and base experiment
#
#
config = {
    # Type of model that the rest of these parameters apply to.
    'model': "CLA",

    # Version that specifies the format of the config.
    'version': 1,

    # Intermediate variables used to compute fields in modelParams and also
    # referenced from the control section.
    'aggregationInfo': {   'days': 0,
    'fields': [],
    'hours': 0,
    'microseconds': 0,
    'milliseconds': 0,
    'minutes': 0,
    'months': 0,
    'seconds': 0,
    'weeks': 0,
    'years': 0},
    'predictAheadTime': None,

    # Model parameter dictionary.
    'modelParams': {
        # The type of inference that this model will perform
        'inferenceType': 'TemporalMultiStep',

        'sensorParams': {
            # Sensor diagnostic output verbosity control;
            # if > 0: sensor region will print out on screen what it's sensing
            # at each step 0: silent; >=1: some info; >=2: more info;
            # >=3: even more info (see compute() in py/regions/RecordSensor.py)
            'verbosity' : 0,

            # Example:
            #     'encoders': {'field1': {'fieldname': 'field1', 'n':100,
            #                  'name': 'field1', 'type': 'AdaptiveScalarEncoder',
            #                  'w': 21}}
            #
            'encoders': {
                u'GList1':     {   'clipInput': True,
    'fieldname': u'GList1',
    'n': 100,
    'name': u'GList1',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'PList':     {   'clipInput': True,
    'fieldname': u'PList',
    'n': 100,
    'name': u'PList',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'Servo1':     {   'clipInput': True,
    'fieldname': u'Servo1',
    'n': 100,
    'name': u'Servo1',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'Servo2':     {   'clipInput': True,
    'fieldname': u'Servo2',
    'n': 100,
    'name': u'Servo2',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'Servo3':     {   'clipInput': True,
    'fieldname': u'Servo3',
    'n': 100,
    'name': u'Servo3',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'Servo5':     {   'clipInput': True,
    'fieldname': u'Servo5',
    'n': 100,
    'name': u'Servo5',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'ReadError1':     {   'clipInput': True,
    'fieldname': u'ReadError1',
    'n': 100,
    'name': u'ReadError1',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'ReadError2':     {   'clipInput': True,
    'fieldname': u'ReadError2',
    'n': 100,
    'name': u'ReadError2',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'ReadError3':     {   'clipInput': True,
    'fieldname': u'ReadError3',
    'n': 100,
    'name': u'ReadError3',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'FlyHeight5':     {   'clipInput': True,
    'fieldname': u'FlyHeight5',
    'n': 100,
    'name': u'FlyHeight5',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'FlyHeight6':     {   'clipInput': True,
    'fieldname': u'FlyHeight6',
    'n': 100,
    'name': u'FlyHeight6',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'FlyHeight7':     {   'clipInput': True,
    'fieldname': u'FlyHeight7',
    'n': 100,
    'name': u'FlyHeight7',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'FlyHeight8':     {   'clipInput': True,
    'fieldname': u'FlyHeight8',
    'n': 100,
    'name': u'FlyHeight8',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'FlyHeight9':     {   'clipInput': True,
    'fieldname': u'FlyHeight9',
    'n': 100,
    'name': u'FlyHeight9',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'FlyHeight10':     {   'clipInput': True,
    'fieldname': u'FlyHeight10',
    'n': 100,
    'name': u'FlyHeight10',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'FlyHeight11':     {   'clipInput': True,
    'fieldname': u'FlyHeight11',
    'n': 100,
    'name': u'FlyHeight11',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'FlyHeight12':     {   'clipInput': True,
    'fieldname': u'FlyHeight12',
    'n': 100,
    'name': u'FlyHeight12',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'ReadError18':     {   'clipInput': True,
    'fieldname': u'ReadError18',
    'n': 100,
    'name': u'ReadError18',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'ReadError19':     {   'clipInput': True,
    'fieldname': u'ReadError19',
    'n': 100,
    'name': u'ReadError19',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'Servo7':     {   'clipInput': True,
    'fieldname': u'Servo7',
    'n': 100,
    'name': u'Servo7',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'Servo8':     {   'clipInput': True,
    'fieldname': u'Servo8',
    'n': 100,
    'name': u'Servo8',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'ReadError20':     {   'clipInput': True,
    'fieldname': u'ReadError20',
    'n': 100,
    'name': u'ReadError20',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'GList2':     {   'clipInput': True,
    'fieldname': u'GList2',
    'n': 100,
    'name': u'GList2',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'GList3':     {   'clipInput': True,
    'fieldname': u'GList3',
    'n': 100,
    'name': u'GList3',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'Servo10':     {   'clipInput': True,
    'fieldname': u'Servo10',
    'n': 100,
    'name': u'Servo10',
    'type': 'AdaptiveScalarEncoder',
    'w': 21},
  u'class':     {   'fieldname': u'class',
    'n': 121,
    'name': u'class',
    'type': 'SDRCategoryEncoder',
    'w': 21},
  '_classifierInput':     {   'classifierOnly': True,
    'fieldname': u'class',
    'n': 121,
    'name': '_classifierInput',
    'type': 'SDRCategoryEncoder',
    'w': 21},
            },

            # A dictionary specifying the period for automatically-generated
            # resets from a RecordSensor;
            #
            # None = disable automatically-generated resets (also disabled if
            # all of the specified values evaluate to 0).
            # Valid keys is the desired combination of the following:
            #   days, hours, minutes, seconds, milliseconds, microseconds, weeks
            #
            # Example for 1.5 days: sensorAutoReset = dict(days=1,hours=12),
            #
            # (value generated from SENSOR_AUTO_RESET)
            'sensorAutoReset' : None,
        },

        'spEnable': True,

        'spParams': {
            # Spatial pooler implementation to use. 
            # Options: "py" (slow, good for debugging), and "cpp" (optimized).
            'spatialImp': 'cpp',

            # SP diagnostic output verbosity control;
            # 0: silent; >=1: some info; >=2: more info;
            'spVerbosity' : 0,

            'globalInhibition': 1,

            # Number of cell columns in the cortical region (same number for
            # SP and TP)
            # (see also tpNCellsPerCol)
            'columnCount': 2048,

            'inputWidth': 0,

            # SP inhibition control (absolute value);
            # Maximum number of active columns in the SP region's output (when
            # there are more, the weaker ones are suppressed)
            'numActiveColumnsPerInhArea': 40,

            'seed': 1956,

            # potentialPct
            # What percent of the columns's receptive field is available
            # for potential synapses. 
            'potentialPct': 0.8,

            # The default connected threshold. Any synapse whose
            # permanence value is above the connected threshold is
            # a "connected synapse", meaning it can contribute to the
            # cell's firing. Typical value is 0.10. Cells whose activity
            # level before inhibition falls below minDutyCycleBeforeInh
            # will have their own internal synPermConnectedCell
            # threshold set below this default value.
            # (This concept applies to both SP and TP and so 'cells'
            # is correct here as opposed to 'columns')
            'synPermConnected': 0.1,

            'synPermActiveInc': 0.05,

            'synPermInactiveDec': 0.0005,
            
            'maxBoost': 2.0
        },

        # Controls whether TP is enabled or disabled;
        # TP is necessary for making temporal predictions, such as predicting
        # the next inputs.  Without TP, the model is only capable of
        # reconstructing missing sensor inputs (via SP).
        'tpEnable' : True,

        'tpParams': {
            # TP diagnostic output verbosity control;
            # 0: silent; [1..6]: increasing levels of verbosity
            # (see verbosity in nupic/trunk/py/nupic/research/TP.py and TP10X*.py)
            'verbosity': 0,

            # Number of cell columns in the cortical region (same number for
            # SP and TP)
            # (see also tpNCellsPerCol)
            'columnCount': 2048,

            # The number of cells (i.e., states), allocated per column.
            'cellsPerColumn': 32,

            'inputWidth': 2048,

            'seed': 1960,

            # Temporal Pooler implementation selector (see _getTPClass in
            # CLARegion.py).
            'temporalImp': 'cpp',

            # New Synapse formation count
            # NOTE: If None, use spNumActivePerInhArea
            'newSynapseCount': 20,

            # Maximum number of synapses per segment
            'maxSynapsesPerSegment': 32,

            # Maximum number of segments per cell
            'maxSegmentsPerCell': 128,

            # Initial Permanence
            'initialPerm': 0.21,

            # Permanence Increment
            'permanenceInc': 0.1,

            # Permanence Decrement
            # If set to None, will automatically default to tpPermanenceInc
            # value.
            'permanenceDec' : 0.1,

            'globalDecay': 0.0,

            'maxAge': 0,

            # Minimum number of active synapses for a segment to be considered
            # during search for the best-matching segments.
            # None=use default
            # Replaces: tpMinThreshold
            'minThreshold': 12,

            # Segment activation threshold.
            # A segment is active if it has >= tpSegmentActivationThreshold
            # connected synapses that are active due to infActiveState
            # None=use default
            # Replaces: tpActivationThreshold
            'activationThreshold': 16,

            'outputType': 'normal',

            # "Pay Attention Mode" length. This tells the TP how many new
            # elements to append to the end of a learned sequence at a time.
            # Smaller values are better for datasets with short sequences,
            # higher values are better for datasets with long sequences.
            'pamLength': 1,
        },

        'clParams': {
            'regionName' : 'CLAClassifierRegion',
            
            # Classifier diagnostic output verbosity control;
            # 0: silent; [1..6]: increasing levels of verbosity
            'clVerbosity' : 0,

            # This controls how fast the classifier learns/forgets. Higher values
            # make it adapt faster and forget older patterns faster.
            'alpha': 0.001,

            # This is set after the call to updateConfigFromSubConfig and is
            # computed from the aggregationInfo and predictAheadTime.
            'steps': '1',
        },

        'anomalyParams': {   u'anomalyCacheRecords': None,
    u'autoDetectThreshold': None,
    u'autoDetectWaitRecords': None},

        'trainSPNetOnlyIfRequested': False,
    },
}
# end of config dictionary


# Adjust base config dictionary for any modifications if imported from a
# sub-experiment
updateConfigFromSubConfig(config)


# Compute predictionSteps based on the predictAheadTime and the aggregation
# period, which may be permuted over.
if config['predictAheadTime'] is not None:
  predictionSteps = int(round(aggregationDivide(
      config['predictAheadTime'], config['aggregationInfo'])))
  assert (predictionSteps >= 1)
  config['modelParams']['clParams']['steps'] = str(predictionSteps)


# Adjust config by applying ValueGetterBase-derived
# futures. NOTE: this MUST be called after updateConfigFromSubConfig() in order
# to support value-getter-based substitutions from the sub-experiment (if any)
applyValueGettersToContainer(config)



control = {
  # The environment that the current model is being run in
  "environment": 'nupic',

  # Input stream specification per py/nupic/frameworks/opf/jsonschema/stream_def.json.
  #
  'dataset' : {   u'info': u'hardrive',
        u'streams': [   {   u'columns': [u'*'],
                            u'info': u'harddrive-smart-data-pp-to-train.csv',
                            u'source': u'file://harddrive-smart-data-pp-to-train.csv'}],
        u'version': 1},

  # Iteration count: maximum number of iterations.  Each iteration corresponds
  # to one record from the (possibly aggregated) dataset.  The task is
  # terminated when either number of iterations reaches iterationCount or
  # all records in the (possibly aggregated) database have been processed,
  # whichever occurs first.
  #
  # iterationCount of -1 = iterate over the entire dataset
  'iterationCount' : 10,


  # A dictionary containing all the supplementary parameters for inference
  "inferenceArgs":{u'inputPredictedField': 'yes',
 u'predictedField': u'class',
 u'predictionSteps': [1]},

  # Metrics: A list of MetricSpecs that instantiate the metrics that are
  # computed for this experiment
  'metrics':[
    MetricSpec(field=u'class', metric='multiStep', inferenceElement='multiStepBestPredictions', params={'window': 1000, 'steps': [1], 'errorMetric': 'avg_err'})
  ],

  # Logged Metrics: A sequence of regular expressions that specify which of
  # the metrics from the Inference Specifications section MUST be logged for
  # every prediction. The regex's correspond to the automatically generated
  # metric labels. This is similar to the way the optimization metric is
  # specified in permutations.py.
  'loggedMetrics': ['.*'],
}



descriptionInterface = ExperimentDescriptionAPI(modelConfig=config,
                                                control=control)
