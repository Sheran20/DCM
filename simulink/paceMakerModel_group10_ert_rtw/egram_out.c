/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: egram_out.c
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

#include "egram_out.h"

/* Include model header file for global data */
#include "paceMakerModel_group10.h"
#include "paceMakerModel_group10_private.h"

/* Forward declaration for local functions */
static void paceMakerModel_SystemCore_setup(freedomk64f_SCIWrite_paceMake_T *obj);
static void paceMakerM_SystemCore_release_b(const
  freedomk64f_AnalogInput_paceM_T *obj);
static void paceMakerMo_SystemCore_delete_l(const
  freedomk64f_AnalogInput_paceM_T *obj);
static void matlabCodegenHandle_matlabCod_f(freedomk64f_AnalogInput_paceM_T *obj);
static void paceMakerMod_SystemCore_release(const
  freedomk64f_SCIWrite_paceMake_T *obj);
static void paceMakerMode_SystemCore_delete(const
  freedomk64f_SCIWrite_paceMake_T *obj);
static void matlabCodegenHandle_matlabCodeg(freedomk64f_SCIWrite_paceMake_T *obj);
static void paceMakerModel_SystemCore_setup(freedomk64f_SCIWrite_paceMake_T *obj)
{
  uint32_T RxPinLoc;
  uint32_T SCIModuleLoc;
  MW_SCI_StopBits_Type StopBitsValue;
  MW_SCI_Parity_Type ParityValue;
  obj->isSetupComplete = false;
  obj->isInitialized = 1;
  RxPinLoc = MW_UNDEFINED_VALUE;
  SCIModuleLoc = 0;
  obj->MW_SCIHANDLE = MW_SCI_Open(&SCIModuleLoc, false, RxPinLoc, 10U);
  MW_SCI_SetBaudrate(obj->MW_SCIHANDLE, 115200U);
  StopBitsValue = MW_SCI_STOPBITS_1;
  ParityValue = MW_SCI_PARITY_NONE;
  MW_SCI_SetFrameFormat(obj->MW_SCIHANDLE, 8, ParityValue, StopBitsValue);
  obj->isSetupComplete = true;
}

static void paceMakerM_SystemCore_release_b(const
  freedomk64f_AnalogInput_paceM_T *obj)
{
  if ((obj->isInitialized == 1) && obj->isSetupComplete) {
    MW_AnalogIn_Stop(obj->MW_ANALOGIN_HANDLE);
    MW_AnalogIn_Close(obj->MW_ANALOGIN_HANDLE);
  }
}

static void paceMakerMo_SystemCore_delete_l(const
  freedomk64f_AnalogInput_paceM_T *obj)
{
  paceMakerM_SystemCore_release_b(obj);
}

static void matlabCodegenHandle_matlabCod_f(freedomk64f_AnalogInput_paceM_T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    paceMakerMo_SystemCore_delete_l(obj);
  }
}

static void paceMakerMod_SystemCore_release(const
  freedomk64f_SCIWrite_paceMake_T *obj)
{
  if ((obj->isInitialized == 1) && obj->isSetupComplete) {
    MW_SCI_Close(obj->MW_SCIHANDLE);
  }
}

static void paceMakerMode_SystemCore_delete(const
  freedomk64f_SCIWrite_paceMake_T *obj)
{
  paceMakerMod_SystemCore_release(obj);
}

static void matlabCodegenHandle_matlabCodeg(freedomk64f_SCIWrite_paceMake_T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    paceMakerMode_SystemCore_delete(obj);
  }
}

/* System initialize for Simulink Function: '<S6>/Simulink Function' */
void egram_out_Init(void)
{
  freedomk64f_AnalogInput_paceM_T *obj;
  MW_AnalogIn_TriggerSource_Type trigger_val;

  /* Start for MATLABSystem: '<S7>/ATR_SIGNAL' */
  paceMakerModel_group10_DW.obj_m.matlabCodegenIsDeleted = true;
  paceMakerModel_group10_DW.obj_m.isInitialized = 0;
  paceMakerModel_group10_DW.obj_m.SampleTime = -1.0;
  paceMakerModel_group10_DW.obj_m.matlabCodegenIsDeleted = false;
  paceMakerModel_group10_DW.obj_m.SampleTime =
    paceMakerModel_group10_P.ATR_SIGNAL_SampleTime;
  obj = &paceMakerModel_group10_DW.obj_m;
  paceMakerModel_group10_DW.obj_m.isSetupComplete = false;
  paceMakerModel_group10_DW.obj_m.isInitialized = 1;
  obj->MW_ANALOGIN_HANDLE = MW_AnalogInSingle_Open(16U);
  trigger_val = MW_ANALOGIN_SOFTWARE_TRIGGER;
  MW_AnalogIn_SetTriggerSource
    (paceMakerModel_group10_DW.obj_m.MW_ANALOGIN_HANDLE, trigger_val, 0U);
  paceMakerModel_group10_DW.obj_m.isSetupComplete = true;

  /* Start for MATLABSystem: '<S7>/VENT_SIGNAL' */
  paceMakerModel_group10_DW.obj_mc.matlabCodegenIsDeleted = true;
  paceMakerModel_group10_DW.obj_mc.isInitialized = 0;
  paceMakerModel_group10_DW.obj_mc.SampleTime = -1.0;
  paceMakerModel_group10_DW.obj_mc.matlabCodegenIsDeleted = false;
  paceMakerModel_group10_DW.obj_mc.SampleTime =
    paceMakerModel_group10_P.VENT_SIGNAL_SampleTime;
  obj = &paceMakerModel_group10_DW.obj_mc;
  paceMakerModel_group10_DW.obj_mc.isSetupComplete = false;
  paceMakerModel_group10_DW.obj_mc.isInitialized = 1;
  obj->MW_ANALOGIN_HANDLE = MW_AnalogInSingle_Open(17U);
  trigger_val = MW_ANALOGIN_SOFTWARE_TRIGGER;
  MW_AnalogIn_SetTriggerSource
    (paceMakerModel_group10_DW.obj_mc.MW_ANALOGIN_HANDLE, trigger_val, 0U);
  paceMakerModel_group10_DW.obj_mc.isSetupComplete = true;

  /* Start for MATLABSystem: '<S7>/Serial Transmit' */
  paceMakerModel_group10_DW.obj_j.isInitialized = 0;
  paceMakerModel_group10_DW.obj_j.matlabCodegenIsDeleted = false;
  paceMakerModel_SystemCore_setup(&paceMakerModel_group10_DW.obj_j);
}

/* Output and update for Simulink Function: '<S6>/Simulink Function' */
void egram_out(void)
{
  uint8_T status;
  uint8_T TxDataLocChar[17];
  uint8_T rtb_TmpSignalConversionAtSerial[17];
  int32_T i;

  /* MATLABSystem: '<S7>/ATR_SIGNAL' */
  if (paceMakerModel_group10_DW.obj_m.SampleTime !=
      paceMakerModel_group10_P.ATR_SIGNAL_SampleTime) {
    paceMakerModel_group10_DW.obj_m.SampleTime =
      paceMakerModel_group10_P.ATR_SIGNAL_SampleTime;
  }

  MW_AnalogIn_Start(paceMakerModel_group10_DW.obj_m.MW_ANALOGIN_HANDLE);
  MW_AnalogInSingle_ReadResult
    (paceMakerModel_group10_DW.obj_m.MW_ANALOGIN_HANDLE,
     &paceMakerModel_group10_B.ATR_SIGNAL, 7);

  /* End of MATLABSystem: '<S7>/ATR_SIGNAL' */

  /* S-Function (any2byte): '<S7>/Byte Pack2' */

  /* Pack: <S7>/Byte Pack2 */
  (void) memcpy(&paceMakerModel_group10_B.BytePack2[0],
                &paceMakerModel_group10_B.ATR_SIGNAL,
                8);

  /* MATLABSystem: '<S7>/VENT_SIGNAL' */
  if (paceMakerModel_group10_DW.obj_mc.SampleTime !=
      paceMakerModel_group10_P.VENT_SIGNAL_SampleTime) {
    paceMakerModel_group10_DW.obj_mc.SampleTime =
      paceMakerModel_group10_P.VENT_SIGNAL_SampleTime;
  }

  MW_AnalogIn_Start(paceMakerModel_group10_DW.obj_mc.MW_ANALOGIN_HANDLE);
  MW_AnalogInSingle_ReadResult
    (paceMakerModel_group10_DW.obj_mc.MW_ANALOGIN_HANDLE,
     &paceMakerModel_group10_B.VENT_SIGNAL, 7);

  /* End of MATLABSystem: '<S7>/VENT_SIGNAL' */

  /* S-Function (any2byte): '<S7>/Byte Pack1' */

  /* Pack: <S7>/Byte Pack1 */
  (void) memcpy(&paceMakerModel_group10_B.BytePack1[0],
                &paceMakerModel_group10_B.VENT_SIGNAL,
                8);

  /* SignalConversion generated from: '<S7>/Serial Transmit' incorporates:
   *  Constant: '<S7>/Constant'
   */
  for (i = 0; i < 8; i++) {
    rtb_TmpSignalConversionAtSerial[i] = paceMakerModel_group10_B.BytePack2[i];
    rtb_TmpSignalConversionAtSerial[i + 8] =
      paceMakerModel_group10_B.BytePack1[i];
  }

  rtb_TmpSignalConversionAtSerial[16] =
    paceMakerModel_group10_P.Constant_Value_c;

  /* End of SignalConversion generated from: '<S7>/Serial Transmit' */

  /* MATLABSystem: '<S7>/Serial Transmit' */
  status = 1U;
  while (status != 0) {
    memcpy((void *)&TxDataLocChar[0], (void *)&rtb_TmpSignalConversionAtSerial[0],
           (uint32_T)((size_t)17 * sizeof(uint8_T)));
    status = MW_SCI_Transmit(paceMakerModel_group10_DW.obj_j.MW_SCIHANDLE,
      TxDataLocChar, 17U);
  }

  /* End of MATLABSystem: '<S7>/Serial Transmit' */
}

/* Termination for Simulink Function: '<S6>/Simulink Function' */
void egram_out_Term(void)
{
  /* Terminate for MATLABSystem: '<S7>/ATR_SIGNAL' */
  matlabCodegenHandle_matlabCod_f(&paceMakerModel_group10_DW.obj_m);

  /* Terminate for MATLABSystem: '<S7>/VENT_SIGNAL' */
  matlabCodegenHandle_matlabCod_f(&paceMakerModel_group10_DW.obj_mc);

  /* Terminate for MATLABSystem: '<S7>/Serial Transmit' */
  matlabCodegenHandle_matlabCodeg(&paceMakerModel_group10_DW.obj_j);
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
