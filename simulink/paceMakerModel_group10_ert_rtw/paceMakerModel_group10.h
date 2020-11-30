/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: paceMakerModel_group10.h
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

#ifndef RTW_HEADER_paceMakerModel_group10_h_
#define RTW_HEADER_paceMakerModel_group10_h_
#include <math.h>
#include <string.h>
#include <stddef.h>
#ifndef paceMakerModel_group10_COMMON_INCLUDES_
# define paceMakerModel_group10_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_PWM.h"
#include "MW_digitalIO.h"
#include "MW_I2C.h"
#include "MW_SCI.h"
#include "MW_AnalogIn.h"
#endif                             /* paceMakerModel_group10_COMMON_INCLUDES_ */

#include "paceMakerModel_group10_types.h"

/* Child system includes */
#include "egram_out_private.h"
#include "egram_out.h"

/* Macros for accessing real-time model data structure */
#ifndef rtmGetErrorStatus
# define rtmGetErrorStatus(rtm)        ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
# define rtmSetErrorStatus(rtm, val)   ((rtm)->errorStatus = (val))
#endif

/* Block signals (default storage) */
typedef struct {
  uint8_T RxDataLocChar[54];
  uint8_T SerialReceive_o1[54];
  real_T FXOS87006AxesSensor[3];
  uint32_T TxPinLoc;
  uint32_T SCIModuleLoc;
  MW_SCI_StopBits_Type StopBitsValue;
  MW_SCI_Parity_Type ParityValue;
  MW_I2C_Mode_Type ModeType;
  uint32_T i2cname;
  real_T ATR_SIGNAL;                   /* '<S7>/ATR_SIGNAL' */
  real_T VENT_SIGNAL;                  /* '<S7>/VENT_SIGNAL' */
  real_T e_ATR_PULSE_WIDTH;            /* '<Root>/DCM_comm' */
  real_T e_VENT_PULSE_WIDTH;           /* '<Root>/DCM_comm' */
  real_T e_RATE_SMOOTH;                /* '<Root>/DCM_comm' */
  real_T d;
  real_T e_act_level;
  real_T d1;
  real_T d2;
  int16_T b_output[3];
  uint8_T output_raw[6];
  real32_T e_PACING_REF_PWM;           /* '<Root>/pacemaker' */
  real32_T e_ATR_AMP;                  /* '<Root>/DCM_comm' */
  real32_T e_VENT_AMP;                 /* '<Root>/DCM_comm' */
  int32_T i;
  int32_T i1;
  int32_T i2;
  int32_T i3;
  uint32_T elapsedTicks;
  uint32_T u;
  uint8_T b_SwappedDataBytes[2];
  int16_T e_ATR_PACE_CTRL;             /* '<Root>/pacemaker' */
  int16_T e_PACE_CHARGE_CTRL;          /* '<Root>/pacemaker' */
  int16_T e_ATR_GND_CTRL;              /* '<Root>/pacemaker' */
  int16_T e_PACE_GND_CTRL;             /* '<Root>/pacemaker' */
  int16_T e_Z_ATR_CTRL;                /* '<Root>/pacemaker' */
  int16_T e_VENT_PACE_CTRL;            /* '<Root>/pacemaker' */
  int16_T e_VENT_GND_CTRL;             /* '<Root>/pacemaker' */
  int16_T e_Z_VENT_CTRL;               /* '<Root>/pacemaker' */
  int16_T e_LOW_RATE_LIM;              /* '<Root>/DCM_comm' */
  int16_T e_ARP;                       /* '<Root>/DCM_comm' */
  int16_T e_VRP;                       /* '<Root>/DCM_comm' */
  int16_T e_AV_DELAY;                  /* '<Root>/DCM_comm' */
  int16_T e_MAX_SENSOR_RATE;           /* '<Root>/DCM_comm' */
  int16_T e_ACT_THRESHOLD;             /* '<Root>/DCM_comm' */
  int16_T e_ACT_REACT_TIME;            /* '<Root>/DCM_comm' */
  int16_T e_ACT_RF;                    /* '<Root>/DCM_comm' */
  int16_T e_ACT_RECOVER_TIME;          /* '<Root>/DCM_comm' */
  uint8_T BytePack2[8];                /* '<S7>/Byte Pack2' */
  uint8_T BytePack1[8];                /* '<S7>/Byte Pack1' */
  uint8_T e_MODE;                      /* '<Root>/DCM_comm' */
  uint8_T e_input_ready;               /* '<Root>/DCM_comm' */
  uint8_T e_ATR_CMP_REF;               /* '<Root>/DCM_comm' */
  uint8_T e_VENT_CMP_REF;              /* '<Root>/DCM_comm' */
  uint8_T b_RegisterValue;
  uint8_T status;
} B_paceMakerModel_group10_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  freedomk64f_fxos8700_paceMake_T obj; /* '<S3>/FXOS8700 6-Axes Sensor' */
  freedomk64f_DigitalRead_paceM_T obj_d;/* '<S4>/VENT_CMP_DETECT' */
  freedomk64f_DigitalRead_paceM_T obj_e;/* '<S1>/ATR_CMP_DETECT' */
  freedomk64f_SCIRead_paceMaker_T obj_p;/* '<S6>/Serial Receive' */
  freedomk64f_AnalogInput_paceM_T obj_m;/* '<S7>/ATR_SIGNAL' */
  freedomk64f_AnalogInput_paceM_T obj_mc;/* '<S7>/VENT_SIGNAL' */
  freedomk64f_PWMOutput_paceMak_T obj_ds;/* '<S4>/VENT_CMP_REF_PWM' */
  freedomk64f_PWMOutput_paceMak_T obj_i;/* '<S3>/PACING_REF_PWM' */
  freedomk64f_PWMOutput_paceMak_T obj_n;/* '<S1>/ATR_CMP_REF_PWM' */
  freedomk64f_DigitalWrite_pace_T obj_l;/* '<S4>/VENT_GND_CTRL' */
  freedomk64f_DigitalWrite_pace_T obj_o;/* '<S4>/VENT_PACE_CTRL' */
  freedomk64f_DigitalWrite_pace_T obj_g;/* '<S4>/Z_VENT_CTRL' */
  freedomk64f_DigitalWrite_pace_T obj_nv;/* '<S3>/PACE_CHARGE_CTRL' */
  freedomk64f_DigitalWrite_pace_T obj_b;/* '<S3>/PACE_GND_CTRL' */
  freedomk64f_DigitalWrite_pace_T obj_n4;/* '<S3>/FRONT_CTRL' */
  freedomk64f_DigitalWrite_pace_T obj_h;/* '<S1>/ATR_GND_CTRL' */
  freedomk64f_DigitalWrite_pace_T obj_ov;/* '<S1>/ATR_PACE_CTRL' */
  freedomk64f_DigitalWrite_pace_T obj_l0;/* '<S1>/Z_ATR_CTRL' */
  freedomk64f_SCIWrite_paceMake_T obj_j;/* '<S7>/Serial Transmit' */
  real_T e_PULSE_WIDTH;                /* '<Root>/pacemaker' */
  real_T e_accel_rec_1;                /* '<Root>/pacemaker' */
  real_T e_accel_rec_2;                /* '<Root>/pacemaker' */
  real_T e_accel_rec_3;                /* '<Root>/pacemaker' */
  real_T e_accel_rec_4;                /* '<Root>/pacemaker' */
  uint32_T temporalCounter_i1;         /* '<Root>/pacemaker' */
  uint32_T previousTicks;              /* '<Root>/pacemaker' */
  int16_T e_PULSE_INT;                 /* '<Root>/pacemaker' */
  int8_T e_accel_rec_count;            /* '<Root>/pacemaker' */
  uint8_T is_c4_paceMakerModel_group10;/* '<Root>/pacemaker' */
  uint8_T is_active_c3_paceMakerModel_gro;/* '<Root>/DCM_comm' */
  uint8_T is_c3_paceMakerModel_group10;/* '<Root>/DCM_comm' */
  uint8_T e_send_req;                  /* '<Root>/DCM_comm' */
} DW_paceMakerModel_group10_T;

/* Parameters (default storage) */
struct P_paceMakerModel_group10_T_ {
  real_T ATR_CMP_DETECT_SampleTime;    /* Expression: SampleTime
                                        * Referenced by: '<S1>/ATR_CMP_DETECT'
                                        */
  real_T FXOS87006AxesSensor_SampleTime;/* Expression: -1
                                         * Referenced by: '<S3>/FXOS8700 6-Axes Sensor'
                                         */
  real_T VENT_CMP_DETECT_SampleTime;   /* Expression: SampleTime
                                        * Referenced by: '<S4>/VENT_CMP_DETECT'
                                        */
  real_T SerialReceive_SampleTime;     /* Expression: -1
                                        * Referenced by: '<S6>/Serial Receive'
                                        */
  real_T VENT_SIGNAL_SampleTime;       /* Expression: SampleTime
                                        * Referenced by: '<S7>/VENT_SIGNAL'
                                        */
  real_T ATR_SIGNAL_SampleTime;        /* Expression: SampleTime
                                        * Referenced by: '<S7>/ATR_SIGNAL'
                                        */
  real_T Constant_Value;               /* Expression: 1
                                        * Referenced by: '<S3>/Constant'
                                        */
  real32_T Gain_Gain;                  /* Computed Parameter: Gain_Gain
                                        * Referenced by: '<S3>/Gain'
                                        */
  uint8_T Gain_Gain_o;                 /* Computed Parameter: Gain_Gain_o
                                        * Referenced by: '<S1>/Gain'
                                        */
  uint8_T Gain_Gain_i;                 /* Computed Parameter: Gain_Gain_i
                                        * Referenced by: '<S4>/Gain'
                                        */
  uint8_T Constant_Value_c;            /* Computed Parameter: Constant_Value_c
                                        * Referenced by: '<S7>/Constant'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_paceMakerModel_group1_T {
  const char_T *errorStatus;

  /*
   * Timing:
   * The following substructure contains information regarding
   * the timing information for the model.
   */
  struct {
    uint32_T clockTick0;
  } Timing;
};

/* Block parameters (default storage) */
extern P_paceMakerModel_group10_T paceMakerModel_group10_P;

/* Block signals (default storage) */
extern B_paceMakerModel_group10_T paceMakerModel_group10_B;

/* Block states (default storage) */
extern DW_paceMakerModel_group10_T paceMakerModel_group10_DW;

/* Model entry point functions */
extern void paceMakerModel_group10_initialize(void);
extern void paceMakerModel_group10_step(void);
extern void paceMakerModel_group10_terminate(void);

/* Real-time Model object */
extern RT_MODEL_paceMakerModel_group_T *const paceMakerModel_group10_M;

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'paceMakerModel_group10'
 * '<S1>'   : 'paceMakerModel_group10/ATR'
 * '<S2>'   : 'paceMakerModel_group10/DCM_comm'
 * '<S3>'   : 'paceMakerModel_group10/PACE'
 * '<S4>'   : 'paceMakerModel_group10/VENT'
 * '<S5>'   : 'paceMakerModel_group10/pacemaker'
 * '<S6>'   : 'paceMakerModel_group10/serialComm'
 * '<S7>'   : 'paceMakerModel_group10/serialComm/Simulink Function'
 */
#endif                                /* RTW_HEADER_paceMakerModel_group10_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
