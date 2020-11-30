/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: paceMakerModel_group10_data.c
 *
 * Code generated for Simulink model 'paceMakerModel_group10'.
 *
 * Model version                  : 1.231
 * Simulink Coder version         : 9.3 (R2020a) 18-Nov-2019
 * C/C++ source code generated on : Sun Nov 29 22:34:00 2020
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "paceMakerModel_group10.h"
#include "paceMakerModel_group10_private.h"

/* Block parameters (default storage) */
P_paceMakerModel_group10_T paceMakerModel_group10_P = {
  /* Expression: SampleTime
   * Referenced by: '<S1>/ATR_CMP_DETECT'
   */
  -1.0,

  /* Expression: -1
   * Referenced by: '<S3>/FXOS8700 6-Axes Sensor'
   */
  -1.0,

  /* Expression: SampleTime
   * Referenced by: '<S4>/VENT_CMP_DETECT'
   */
  -1.0,

  /* Expression: -1
   * Referenced by: '<S6>/Serial Receive'
   */
  -1.0,

  /* Expression: SampleTime
   * Referenced by: '<S7>/VENT_SIGNAL'
   */
  -1.0,

  /* Expression: SampleTime
   * Referenced by: '<S7>/ATR_SIGNAL'
   */
  -1.0,

  /* Expression: 1
   * Referenced by: '<S3>/Constant'
   */
  1.0,

  /* Computed Parameter: Gain_Gain
   * Referenced by: '<S3>/Gain'
   */
  20.0F,

  /* Computed Parameter: Gain_Gain_o
   * Referenced by: '<S1>/Gain'
   */
  160U,

  /* Computed Parameter: Gain_Gain_i
   * Referenced by: '<S4>/Gain'
   */
  160U,

  /* Computed Parameter: Constant_Value_c
   * Referenced by: '<S7>/Constant'
   */
  10U
};

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
