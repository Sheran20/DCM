/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: egram_out_private.h
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

#ifndef RTW_HEADER_egram_out_private_h_
#define RTW_HEADER_egram_out_private_h_
#include <string.h>
#ifndef paceMakerModel_group10_COMMON_INCLUDES_
# define paceMakerModel_group10_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_PWM.h"
#include "MW_digitalIO.h"
#include "MW_I2C.h"
#include "MW_SCI.h"
#include "MW_AnalogIn.h"
#endif                             /* paceMakerModel_group10_COMMON_INCLUDES_ */

extern void egram_out_Init(void);
extern void egram_out_Term(void);

#endif                                 /* RTW_HEADER_egram_out_private_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
