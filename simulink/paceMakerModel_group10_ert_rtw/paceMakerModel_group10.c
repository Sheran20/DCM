/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: paceMakerModel_group10.c
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
#include "rt_roundd_snf.h"

/* Named constants for Chart: '<Root>/DCM_comm' */
#define paceMakerModel__IN_status_check ((uint8_T)4U)
#define paceMakerModel_gr_IN_send_egram ((uint8_T)3U)
#define paceMakerModel_gro_IN_comm_init ((uint8_T)1U)
#define paceMakerModel_group_IN_receive ((uint8_T)2U)

/* Named constants for Chart: '<Root>/pacemaker' */
#define paceMakerMod_IN_RATE_MODULATION ((uint8_T)5U)
#define paceMakerModel_gr_IN_MODE_CHECK ((uint8_T)4U)
#define paceMakerModel_grou_IN_A_Charge ((uint8_T)1U)
#define paceMakerModel_grou_IN_V_Charge ((uint8_T)6U)
#define paceMakerModel_group1_IN_A_Pace ((uint8_T)2U)
#define paceMakerModel_group1_IN_V_Pace ((uint8_T)7U)
#define paceMakerModel_group_IN_A_SENSE ((uint8_T)3U)
#define paceMakerModel_group_IN_V_SENSE ((uint8_T)8U)

/* Block signals (default storage) */
B_paceMakerModel_group10_T paceMakerModel_group10_B;

/* Block states (default storage) */
DW_paceMakerModel_group10_T paceMakerModel_group10_DW;

/* Real-time model */
RT_MODEL_paceMakerModel_group_T paceMakerModel_group10_M_;
RT_MODEL_paceMakerModel_group_T *const paceMakerModel_group10_M =
  &paceMakerModel_group10_M_;

/* Forward declaration for local functions */
static void paceMakerM_enter_atomic_receive(const uint8_T SerialReceive_o1[54]);
static void paceMak_enter_atomic_MODE_CHECK(void);
static void paceMaker_enter_atomic_V_Charge(void);
static void paceMakerModel_group10_A_Charge(void);
static void pa_enter_atomic_RATE_MODULATION(const real_T FXOS87006AxesSensor[3]);
static void paceMaker_enter_atomic_A_Charge(void);
static void paceMakerModel_group10_A_Pace(const real_T FXOS87006AxesSensor[3]);
static void p_SystemCore_rele_p(const freedomk64f_SCIRead_paceMaker_T *obj);
static void p_SystemCore_dele_p(const freedomk64f_SCIRead_paceMaker_T *obj);
static void paceMakerMode_matlabCodegenHa_p(freedomk64f_SCIRead_paceMaker_T *obj);
static void p_SystemCore_release_pbmd0kqiuc(const
  freedomk64f_fxos8700_paceMake_T *obj);
static void pa_SystemCore_delete_pbmd0kqiuc(const
  freedomk64f_fxos8700_paceMake_T *obj);
static void matlabCodegenHandle__pbmd0kqiuc(freedomk64f_fxos8700_paceMake_T *obj);
static void SystemCore_release_pbmd0kqiuc0(b_freedomk64f_I2CMasterWrite__T *obj);
static void p_SystemCore_delete_pbmd0kqiuc0(b_freedomk64f_I2CMasterWrite__T *obj);
static void matlabCodegenHandle_pbmd0kqiuc0(b_freedomk64f_I2CMasterWrite__T *obj);
static void paceMa_SystemCore_release_pbmd0(const
  freedomk64f_DigitalRead_paceM_T *obj);
static void paceMak_SystemCore_delete_pbmd0(const
  freedomk64f_DigitalRead_paceM_T *obj);
static void matlabCodegenHandle_matla_pbmd0(freedomk64f_DigitalRead_paceM_T *obj);
static void paceMaker_SystemCore_release_pb(const
  freedomk64f_DigitalWrite_pace_T *obj);
static void paceMakerM_SystemCore_delete_pb(const
  freedomk64f_DigitalWrite_pace_T *obj);
static void matlabCodegenHandle_matlabCo_pb(freedomk64f_DigitalWrite_pace_T *obj);
static void paceMakerM_SystemCore_release_p(const
  freedomk64f_PWMOutput_paceMak_T *obj);
static void paceMakerMo_SystemCore_delete_p(const
  freedomk64f_PWMOutput_paceMak_T *obj);
static void matlabCodegenHandle_matlabCod_p(freedomk64f_PWMOutput_paceMak_T *obj);
static void paceMakerMo_SystemCore_setup_pb(freedomk64f_SCIRead_paceMaker_T *obj);
static void paceMakerMod_SystemCore_setup_p(freedomk64f_fxos8700_paceMake_T *obj);

/* Function for Chart: '<Root>/DCM_comm' */
static void paceMakerM_enter_atomic_receive(const uint8_T SerialReceive_o1[54])
{
  paceMakerModel_group10_DW.e_send_req = SerialReceive_o1[0];
  if (paceMakerModel_group10_DW.e_send_req == 0) {
    paceMakerModel_group10_B.e_MODE = SerialReceive_o1[1];
    memcpy((void *)&paceMakerModel_group10_B.e_LOW_RATE_LIM, (void *)
           &SerialReceive_o1[2], (uint32_T)((size_t)1 * sizeof(int16_T)));
    memcpy((void *)&paceMakerModel_group10_B.e_ATR_AMP, (void *)
           &SerialReceive_o1[4], (uint32_T)((size_t)1 * sizeof(real32_T)));
    memcpy((void *)&paceMakerModel_group10_B.e_VENT_AMP, (void *)
           &SerialReceive_o1[8], (uint32_T)((size_t)1 * sizeof(real32_T)));
    memcpy((void *)&paceMakerModel_group10_B.e_ATR_PULSE_WIDTH, (void *)
           &SerialReceive_o1[12], (uint32_T)((size_t)1 * sizeof(real_T)));
    memcpy((void *)&paceMakerModel_group10_B.e_VENT_PULSE_WIDTH, (void *)
           &SerialReceive_o1[20], (uint32_T)((size_t)1 * sizeof(real_T)));
    memcpy((void *)&paceMakerModel_group10_B.e_RATE_SMOOTH, (void *)
           &SerialReceive_o1[32], (uint32_T)((size_t)1 * sizeof(real_T)));
    memcpy((void *)&paceMakerModel_group10_B.e_AV_DELAY, (void *)
           &SerialReceive_o1[40], (uint32_T)((size_t)1 * sizeof(int16_T)));
    memcpy((void *)&paceMakerModel_group10_B.e_MAX_SENSOR_RATE, (void *)
           &SerialReceive_o1[44], (uint32_T)((size_t)1 * sizeof(int16_T)));
    memcpy((void *)&paceMakerModel_group10_B.e_ACT_THRESHOLD, (void *)
           &SerialReceive_o1[46], (uint32_T)((size_t)1 * sizeof(int16_T)));
    memcpy((void *)&paceMakerModel_group10_B.e_ACT_REACT_TIME, (void *)
           &SerialReceive_o1[48], (uint32_T)((size_t)1 * sizeof(int16_T)));
    memcpy((void *)&paceMakerModel_group10_B.e_ACT_RF, (void *)
           &SerialReceive_o1[50], (uint32_T)((size_t)1 * sizeof(int16_T)));
    memcpy((void *)&paceMakerModel_group10_B.e_ACT_RECOVER_TIME, (void *)
           &SerialReceive_o1[52], (uint32_T)((size_t)1 * sizeof(int16_T)));
    paceMakerModel_group10_B.e_ATR_CMP_REF = SerialReceive_o1[42];
    paceMakerModel_group10_B.e_VENT_CMP_REF = SerialReceive_o1[43];
    memcpy((void *)&paceMakerModel_group10_B.e_ARP, (void *)&SerialReceive_o1[28],
           (uint32_T)((size_t)1 * sizeof(int16_T)));
    memcpy((void *)&paceMakerModel_group10_B.e_VRP, (void *)&SerialReceive_o1[30],
           (uint32_T)((size_t)1 * sizeof(int16_T)));
    paceMakerModel_group10_B.e_input_ready = 1U;
  }
}

/* Function for Chart: '<Root>/pacemaker' */
static void paceMak_enter_atomic_MODE_CHECK(void)
{
  paceMakerModel_group10_B.d2 = rt_roundd_snf(60000.0 / (real_T)
    paceMakerModel_group10_B.e_LOW_RATE_LIM);
  if (paceMakerModel_group10_B.d2 < 32768.0) {
    if (paceMakerModel_group10_B.d2 >= -32768.0) {
      paceMakerModel_group10_DW.e_PULSE_INT = (int16_T)
        paceMakerModel_group10_B.d2;
    } else {
      paceMakerModel_group10_DW.e_PULSE_INT = MIN_int16_T;
    }
  } else {
    paceMakerModel_group10_DW.e_PULSE_INT = MAX_int16_T;
  }

  if ((paceMakerModel_group10_B.e_MODE == 0) || (paceMakerModel_group10_B.e_MODE
       == 2) || (paceMakerModel_group10_B.e_MODE == 10) ||
      (paceMakerModel_group10_B.e_MODE == 12) ||
      (paceMakerModel_group10_B.e_MODE == 4) || (paceMakerModel_group10_B.e_MODE
       == 14)) {
    paceMakerModel_group10_DW.e_PULSE_WIDTH =
      paceMakerModel_group10_B.e_ATR_PULSE_WIDTH;
    paceMakerModel_group10_B.e_PACING_REF_PWM =
      paceMakerModel_group10_B.e_ATR_AMP;
  } else {
    paceMakerModel_group10_DW.e_PULSE_WIDTH =
      paceMakerModel_group10_B.e_VENT_PULSE_WIDTH;
    paceMakerModel_group10_B.e_PACING_REF_PWM =
      paceMakerModel_group10_B.e_VENT_AMP;
  }

  if ((paceMakerModel_group10_B.e_MODE == 2) || (paceMakerModel_group10_B.e_MODE
       == 3) || (paceMakerModel_group10_B.e_MODE == 12) ||
      (paceMakerModel_group10_B.e_MODE == 13)) {
    paceMakerModel_group10_B.d2 = rt_roundd_snf((real_T)
      paceMakerModel_group10_DW.e_PULSE_INT *
      paceMakerModel_group10_B.e_RATE_SMOOTH);
    if (paceMakerModel_group10_B.d2 < 32768.0) {
      if (paceMakerModel_group10_B.d2 >= -32768.0) {
        paceMakerModel_group10_DW.e_PULSE_INT = (int16_T)
          paceMakerModel_group10_B.d2;
      } else {
        paceMakerModel_group10_DW.e_PULSE_INT = MIN_int16_T;
      }
    } else {
      paceMakerModel_group10_DW.e_PULSE_INT = MAX_int16_T;
    }
  }

  paceMakerModel_group10_DW.e_accel_rec_count = 1;
  paceMakerModel_group10_DW.e_accel_rec_1 = 0.0;
  paceMakerModel_group10_DW.e_accel_rec_2 = 0.0;
  paceMakerModel_group10_DW.e_accel_rec_3 = 0.0;
  paceMakerModel_group10_DW.e_accel_rec_4 = 0.0;
}

/* Function for Chart: '<Root>/pacemaker' */
static void paceMaker_enter_atomic_V_Charge(void)
{
  paceMakerModel_group10_B.e_PACE_CHARGE_CTRL = 1;
  paceMakerModel_group10_B.e_VENT_GND_CTRL = 1;
  paceMakerModel_group10_B.e_VENT_PACE_CTRL = 0;
  paceMakerModel_group10_B.e_PACE_GND_CTRL = 1;
  paceMakerModel_group10_B.e_ATR_PACE_CTRL = 0;
  paceMakerModel_group10_B.e_ATR_GND_CTRL = 0;
  paceMakerModel_group10_B.e_Z_ATR_CTRL = 0;
  paceMakerModel_group10_B.e_Z_VENT_CTRL = 0;
  if ((paceMakerModel_group10_B.e_MODE == 4) || (paceMakerModel_group10_B.e_MODE
       == 14)) {
    paceMakerModel_group10_B.e_PACING_REF_PWM =
      paceMakerModel_group10_B.e_VENT_AMP;
  }
}

/* Function for Chart: '<Root>/pacemaker' */
static void paceMakerModel_group10_A_Charge(void)
{
  int32_T tmp;
  real_T tmp_0;
  int16_T tmp_1;
  boolean_T guard1 = false;
  paceMakerModel_group10_B.e_PACE_CHARGE_CTRL = 1;
  paceMakerModel_group10_B.e_ATR_GND_CTRL = 1;
  paceMakerModel_group10_B.e_ATR_PACE_CTRL = 0;
  paceMakerModel_group10_B.e_PACE_GND_CTRL = 1;
  paceMakerModel_group10_B.e_VENT_PACE_CTRL = 0;
  paceMakerModel_group10_B.e_VENT_GND_CTRL = 0;
  paceMakerModel_group10_B.e_Z_ATR_CTRL = 0;
  paceMakerModel_group10_B.e_Z_VENT_CTRL = 0;
  if ((paceMakerModel_group10_DW.temporalCounter_i1 >= (uint32_T)
       paceMakerModel_group10_B.e_ARP) && ((paceMakerModel_group10_B.e_MODE == 2)
       || (paceMakerModel_group10_B.e_MODE == 12))) {
    paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
      paceMakerModel_group_IN_A_SENSE;
    paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
  } else {
    tmp_0 = rt_roundd_snf((real_T)paceMakerModel_group10_DW.e_PULSE_INT -
                          paceMakerModel_group10_DW.e_PULSE_WIDTH);
    if (tmp_0 < 32768.0) {
      if (tmp_0 >= -32768.0) {
        tmp_1 = (int16_T)tmp_0;
      } else {
        tmp_1 = MIN_int16_T;
      }
    } else {
      tmp_1 = MAX_int16_T;
    }

    guard1 = false;
    if (((paceMakerModel_group10_B.e_MODE == 0) ||
         (paceMakerModel_group10_B.e_MODE == 10)) &&
        (paceMakerModel_group10_DW.temporalCounter_i1 >= (uint32_T)tmp_1)) {
      guard1 = true;
    } else {
      tmp_0 = rt_roundd_snf((real_T)paceMakerModel_group10_DW.e_PULSE_INT -
                            paceMakerModel_group10_B.e_ATR_PULSE_WIDTH);
      if (tmp_0 < 32768.0) {
        if (tmp_0 >= -32768.0) {
          tmp_1 = (int16_T)tmp_0;
        } else {
          tmp_1 = MIN_int16_T;
        }
      } else {
        tmp_1 = MAX_int16_T;
      }

      tmp_0 = rt_roundd_snf((real_T)tmp_1 -
                            paceMakerModel_group10_B.e_VENT_PULSE_WIDTH);
      if (tmp_0 < 32768.0) {
        if (tmp_0 >= -32768.0) {
          tmp_1 = (int16_T)tmp_0;
        } else {
          tmp_1 = MIN_int16_T;
        }
      } else {
        tmp_1 = MAX_int16_T;
      }

      tmp = tmp_1 - paceMakerModel_group10_B.e_AV_DELAY;
      if (tmp > 32767) {
        tmp = 32767;
      } else {
        if (tmp < -32768) {
          tmp = -32768;
        }
      }

      if (((paceMakerModel_group10_B.e_MODE == 4) ||
           (paceMakerModel_group10_B.e_MODE == 14)) &&
          (paceMakerModel_group10_DW.temporalCounter_i1 >= (uint32_T)(int16_T)
           tmp)) {
        guard1 = true;
      } else {
        if (paceMakerModel_group10_B.e_input_ready != 0) {
          paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
            paceMakerModel_gr_IN_MODE_CHECK;
          paceMak_enter_atomic_MODE_CHECK();
        }
      }
    }

    if (guard1) {
      paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
        paceMakerModel_group1_IN_A_Pace;
      paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
      paceMakerModel_group10_B.e_PACE_CHARGE_CTRL = 0;
      paceMakerModel_group10_B.e_ATR_GND_CTRL = 0;
      paceMakerModel_group10_B.e_ATR_PACE_CTRL = 1;
    }
  }
}

/* Function for Chart: '<Root>/pacemaker' */
static void pa_enter_atomic_RATE_MODULATION(const real_T FXOS87006AxesSensor[3])
{
  int16_T z;
  int16_T b_z;
  uint16_T c_y;
  uint16_T d_y;
  uint16_T q;
  int32_T tmp;
  switch (paceMakerModel_group10_DW.e_accel_rec_count) {
   case 1:
    paceMakerModel_group10_DW.e_accel_rec_1 = fabs(FXOS87006AxesSensor[0]) +
      fabs(FXOS87006AxesSensor[1]);
    break;

   case 2:
    paceMakerModel_group10_DW.e_accel_rec_2 = fabs(FXOS87006AxesSensor[0]) +
      fabs(FXOS87006AxesSensor[1]);
    break;

   case 3:
    paceMakerModel_group10_DW.e_accel_rec_3 = fabs(FXOS87006AxesSensor[0]) +
      fabs(FXOS87006AxesSensor[1]);
    break;

   case 4:
    paceMakerModel_group10_DW.e_accel_rec_4 = fabs(FXOS87006AxesSensor[0]) +
      fabs(FXOS87006AxesSensor[1]);
    break;
  }

  if (paceMakerModel_group10_DW.e_accel_rec_count >= 4) {
    paceMakerModel_group10_DW.e_accel_rec_count = 1;
  } else {
    tmp = paceMakerModel_group10_DW.e_accel_rec_count + 1;
    if (tmp > 127) {
      tmp = 127;
    }

    paceMakerModel_group10_DW.e_accel_rec_count = (int8_T)tmp;
  }

  paceMakerModel_group10_B.e_act_level =
    ((((paceMakerModel_group10_DW.e_accel_rec_1 +
        paceMakerModel_group10_DW.e_accel_rec_2) +
       paceMakerModel_group10_DW.e_accel_rec_3) +
      paceMakerModel_group10_DW.e_accel_rec_4) / 4.0 - 0.1) * 20.0;
  if (paceMakerModel_group10_B.e_act_level >
      paceMakerModel_group10_B.e_ACT_THRESHOLD) {
    paceMakerModel_group10_B.e_act_level = rt_roundd_snf
      (paceMakerModel_group10_B.e_act_level - (real_T)
       paceMakerModel_group10_B.e_ACT_THRESHOLD);
    tmp = paceMakerModel_group10_B.e_MAX_SENSOR_RATE -
      paceMakerModel_group10_B.e_LOW_RATE_LIM;
    paceMakerModel_group10_B.i1 = tmp;
    if (tmp > 32767) {
      paceMakerModel_group10_B.i1 = 32767;
    } else {
      if (tmp < -32768) {
        paceMakerModel_group10_B.i1 = -32768;
      }
    }

    if (paceMakerModel_group10_B.e_act_level < 32768.0) {
      if (paceMakerModel_group10_B.e_act_level >= -32768.0) {
        z = (int16_T)paceMakerModel_group10_B.e_act_level;
      } else {
        z = MIN_int16_T;
      }
    } else {
      z = MAX_int16_T;
    }

    paceMakerModel_group10_B.i1 *= z;
    if (paceMakerModel_group10_B.i1 > 32767) {
      paceMakerModel_group10_B.i1 = 32767;
    } else {
      if (paceMakerModel_group10_B.i1 < -32768) {
        paceMakerModel_group10_B.i1 = -32768;
      }
    }

    if (paceMakerModel_group10_B.e_ACT_RF > 16383) {
      z = MAX_int16_T;
    } else if (paceMakerModel_group10_B.e_ACT_RF <= -16384) {
      z = MIN_int16_T;
    } else {
      z = (int16_T)(paceMakerModel_group10_B.e_ACT_RF << 1);
    }

    paceMakerModel_group10_B.i3 = 40 - z;
    if (paceMakerModel_group10_B.i3 > 32767) {
      paceMakerModel_group10_B.i3 = 32767;
    }

    switch ((int16_T)paceMakerModel_group10_B.i3) {
     case 0:
      if ((int16_T)paceMakerModel_group10_B.i1 == 0) {
        z = 0;
      } else if ((int16_T)paceMakerModel_group10_B.i1 < 0) {
        z = MIN_int16_T;
      } else {
        z = MAX_int16_T;
      }
      break;

     case 1:
      z = (int16_T)paceMakerModel_group10_B.i1;
      break;

     case -1:
      paceMakerModel_group10_B.i1 = -(int16_T)paceMakerModel_group10_B.i1;
      if (paceMakerModel_group10_B.i1 > 32767) {
        paceMakerModel_group10_B.i1 = 32767;
      }

      z = (int16_T)paceMakerModel_group10_B.i1;
      break;

     default:
      if ((int16_T)paceMakerModel_group10_B.i1 >= 0) {
        c_y = (uint16_T)paceMakerModel_group10_B.i1;
      } else if ((int16_T)paceMakerModel_group10_B.i1 == -32768) {
        c_y = 32768U;
      } else {
        c_y = (uint16_T)-(int16_T)paceMakerModel_group10_B.i1;
      }

      if ((int16_T)paceMakerModel_group10_B.i3 >= 0) {
        d_y = (uint16_T)paceMakerModel_group10_B.i3;
      } else {
        d_y = (uint16_T)-(int16_T)paceMakerModel_group10_B.i3;
      }

      q = (uint16_T)(d_y == 0U ? MAX_uint32_T : (uint32_T)c_y / d_y);
      c_y = (uint16_T)((uint32_T)c_y - (uint16_T)((uint32_T)q * d_y));
      if ((c_y > 0) && (c_y >= (int32_T)((uint32_T)d_y >> 1) + (d_y & 1))) {
        q++;
      }

      z = (int16_T)q;
      if (((int16_T)paceMakerModel_group10_B.i1 < 0) != ((int16_T)
           paceMakerModel_group10_B.i3 < 0)) {
        z = (int16_T)-(int16_T)q;
      }
      break;
    }

    paceMakerModel_group10_B.i1 = paceMakerModel_group10_B.e_LOW_RATE_LIM + z;
    if (paceMakerModel_group10_B.i1 > 32767) {
      paceMakerModel_group10_B.i1 = 32767;
    } else {
      if (paceMakerModel_group10_B.i1 < -32768) {
        paceMakerModel_group10_B.i1 = -32768;
      }
    }

    paceMakerModel_group10_B.i3 = paceMakerModel_group10_B.e_ACT_REACT_TIME *
      1000;
    if (paceMakerModel_group10_B.i3 > 32767) {
      paceMakerModel_group10_B.i3 = 32767;
    } else {
      if (paceMakerModel_group10_B.i3 < -32768) {
        paceMakerModel_group10_B.i3 = -32768;
      }
    }

    paceMakerModel_group10_B.i1 = (int16_T)paceMakerModel_group10_B.i1 -
      paceMakerModel_group10_B.e_LOW_RATE_LIM;
    paceMakerModel_group10_B.i2 = paceMakerModel_group10_B.i1;
    if (paceMakerModel_group10_B.i1 > 32767) {
      paceMakerModel_group10_B.i2 = 32767;
    } else {
      if (paceMakerModel_group10_B.i1 < -32768) {
        paceMakerModel_group10_B.i2 = -32768;
      }
    }

    paceMakerModel_group10_B.i3 *= paceMakerModel_group10_B.i2;
    if (paceMakerModel_group10_B.i3 > 32767) {
      paceMakerModel_group10_B.i3 = 32767;
    } else {
      if (paceMakerModel_group10_B.i3 < -32768) {
        paceMakerModel_group10_B.i3 = -32768;
      }
    }

    if (tmp > 32767) {
      tmp = 32767;
    } else {
      if (tmp < -32768) {
        tmp = -32768;
      }
    }

    paceMakerModel_group10_B.e_act_level = rt_roundd_snf((real_T)
      paceMakerModel_group10_B.i3 / (real_T)tmp);
    if (paceMakerModel_group10_B.e_act_level < 32768.0) {
      if (paceMakerModel_group10_B.e_act_level >= -32768.0) {
        z = (int16_T)paceMakerModel_group10_B.e_act_level;
      } else {
        z = MIN_int16_T;
      }
    } else {
      z = MAX_int16_T;
    }

    tmp = 1000 * z;
    if (tmp > 32767) {
      tmp = 32767;
    } else {
      if (tmp < -32768) {
        tmp = -32768;
      }
    }

    if (paceMakerModel_group10_B.i1 > 32767) {
      paceMakerModel_group10_B.i1 = 32767;
    } else {
      if (paceMakerModel_group10_B.i1 < -32768) {
        paceMakerModel_group10_B.i1 = -32768;
      }
    }

    paceMakerModel_group10_B.i1 *= paceMakerModel_group10_DW.e_PULSE_INT;
    if (paceMakerModel_group10_B.i1 > 32767) {
      paceMakerModel_group10_B.i1 = 32767;
    } else {
      if (paceMakerModel_group10_B.i1 < -32768) {
        paceMakerModel_group10_B.i1 = -32768;
      }
    }

    switch ((int16_T)tmp) {
     case 0:
      if ((int16_T)paceMakerModel_group10_B.i1 == 0) {
        b_z = 0;
      } else if ((int16_T)paceMakerModel_group10_B.i1 < 0) {
        b_z = MIN_int16_T;
      } else {
        b_z = MAX_int16_T;
      }
      break;

     case 1:
      b_z = (int16_T)paceMakerModel_group10_B.i1;
      break;

     case -1:
      tmp = -(int16_T)paceMakerModel_group10_B.i1;
      if (tmp > 32767) {
        tmp = 32767;
      }

      b_z = (int16_T)tmp;
      break;

     default:
      if ((int16_T)paceMakerModel_group10_B.i1 >= 0) {
        c_y = (uint16_T)paceMakerModel_group10_B.i1;
      } else if ((int16_T)paceMakerModel_group10_B.i1 == -32768) {
        c_y = 32768U;
      } else {
        c_y = (uint16_T)-(int16_T)paceMakerModel_group10_B.i1;
      }

      if ((int16_T)tmp >= 0) {
        d_y = (uint16_T)tmp;
      } else if ((int16_T)tmp == -32768) {
        d_y = 32768U;
      } else {
        d_y = (uint16_T)-(int16_T)tmp;
      }

      q = (uint16_T)(d_y == 0U ? MAX_uint32_T : (uint32_T)c_y / d_y);
      c_y = (uint16_T)((uint32_T)c_y - (uint16_T)((uint32_T)q * d_y));
      if ((c_y > 0) && (c_y >= (int32_T)((uint32_T)d_y >> 1) + (d_y & 1))) {
        q++;
      }

      b_z = (int16_T)q;
      if (((int16_T)paceMakerModel_group10_B.i1 < 0) != ((int16_T)tmp < 0)) {
        b_z = (int16_T)-(int16_T)q;
      }
      break;
    }

    paceMakerModel_group10_B.e_act_level = rt_roundd_snf(60000.0 / (real_T)
      paceMakerModel_group10_DW.e_PULSE_INT);
    if (paceMakerModel_group10_B.e_act_level < 32768.0) {
      if (paceMakerModel_group10_B.e_act_level >= -32768.0) {
        z = (int16_T)paceMakerModel_group10_B.e_act_level;
      } else {
        z = MIN_int16_T;
      }
    } else {
      z = MAX_int16_T;
    }

    tmp = b_z + z;
    if (tmp > 32767) {
      tmp = 32767;
    } else {
      if (tmp < -32768) {
        tmp = -32768;
      }
    }

    paceMakerModel_group10_B.e_act_level = rt_roundd_snf(60000.0 / (real_T)tmp);
    if (paceMakerModel_group10_B.e_act_level < 32768.0) {
      if (paceMakerModel_group10_B.e_act_level >= -32768.0) {
        paceMakerModel_group10_DW.e_PULSE_INT = (int16_T)
          paceMakerModel_group10_B.e_act_level;
      } else {
        paceMakerModel_group10_DW.e_PULSE_INT = MIN_int16_T;
      }
    } else {
      paceMakerModel_group10_DW.e_PULSE_INT = MAX_int16_T;
    }

    paceMakerModel_group10_B.e_act_level = rt_roundd_snf(60000.0 / (real_T)
      paceMakerModel_group10_DW.e_PULSE_INT);
    if (paceMakerModel_group10_B.e_act_level < 32768.0) {
      if (paceMakerModel_group10_B.e_act_level >= -32768.0) {
        z = (int16_T)paceMakerModel_group10_B.e_act_level;
      } else {
        z = MIN_int16_T;
      }
    } else {
      z = MAX_int16_T;
    }

    if (z > paceMakerModel_group10_B.e_MAX_SENSOR_RATE) {
      paceMakerModel_group10_B.e_act_level = rt_roundd_snf(60000.0 / (real_T)
        paceMakerModel_group10_B.e_MAX_SENSOR_RATE);
      if (paceMakerModel_group10_B.e_act_level < 32768.0) {
        if (paceMakerModel_group10_B.e_act_level >= -32768.0) {
          paceMakerModel_group10_DW.e_PULSE_INT = (int16_T)
            paceMakerModel_group10_B.e_act_level;
        } else {
          paceMakerModel_group10_DW.e_PULSE_INT = MIN_int16_T;
        }
      } else {
        paceMakerModel_group10_DW.e_PULSE_INT = MAX_int16_T;
      }
    }
  } else {
    paceMakerModel_group10_B.e_act_level = 60000.0 / (real_T)
      paceMakerModel_group10_DW.e_PULSE_INT;
    paceMakerModel_group10_B.d1 = rt_roundd_snf
      (paceMakerModel_group10_B.e_act_level);
    if (paceMakerModel_group10_B.d1 < 32768.0) {
      if (paceMakerModel_group10_B.d1 >= -32768.0) {
        z = (int16_T)paceMakerModel_group10_B.d1;
      } else {
        z = MIN_int16_T;
      }
    } else {
      z = MAX_int16_T;
    }

    if (z > paceMakerModel_group10_B.e_LOW_RATE_LIM) {
      tmp = paceMakerModel_group10_B.e_MAX_SENSOR_RATE -
        paceMakerModel_group10_B.e_LOW_RATE_LIM;
      if (tmp > 32767) {
        tmp = 32767;
      } else {
        if (tmp < -32768) {
          tmp = -32768;
        }
      }

      paceMakerModel_group10_B.i1 = paceMakerModel_group10_B.e_ACT_RECOVER_TIME *
        1000;
      if (paceMakerModel_group10_B.i1 > 32767) {
        paceMakerModel_group10_B.i1 = 32767;
      } else {
        if (paceMakerModel_group10_B.i1 < -32768) {
          paceMakerModel_group10_B.i1 = -32768;
        }
      }

      paceMakerModel_group10_B.e_act_level = rt_roundd_snf(60000.0 /
        (paceMakerModel_group10_B.e_act_level - (real_T)(tmp *
        paceMakerModel_group10_DW.e_PULSE_INT) / (real_T)
         paceMakerModel_group10_B.i1));
      if (paceMakerModel_group10_B.e_act_level < 32768.0) {
        if (paceMakerModel_group10_B.e_act_level >= -32768.0) {
          paceMakerModel_group10_DW.e_PULSE_INT = (int16_T)
            paceMakerModel_group10_B.e_act_level;
        } else {
          paceMakerModel_group10_DW.e_PULSE_INT = MIN_int16_T;
        }
      } else {
        paceMakerModel_group10_DW.e_PULSE_INT = MAX_int16_T;
      }
    }
  }
}

/* Function for Chart: '<Root>/pacemaker' */
static void paceMaker_enter_atomic_A_Charge(void)
{
  paceMakerModel_group10_B.e_PACE_CHARGE_CTRL = 1;
  paceMakerModel_group10_B.e_ATR_GND_CTRL = 1;
  paceMakerModel_group10_B.e_ATR_PACE_CTRL = 0;
  paceMakerModel_group10_B.e_PACE_GND_CTRL = 1;
  paceMakerModel_group10_B.e_VENT_PACE_CTRL = 0;
  paceMakerModel_group10_B.e_VENT_GND_CTRL = 0;
  paceMakerModel_group10_B.e_Z_ATR_CTRL = 0;
  paceMakerModel_group10_B.e_Z_VENT_CTRL = 0;
  if ((paceMakerModel_group10_B.e_MODE == 4) || (paceMakerModel_group10_B.e_MODE
       == 14)) {
    paceMakerModel_group10_B.e_PACING_REF_PWM =
      paceMakerModel_group10_B.e_ATR_AMP;
  }
}

/* Function for Chart: '<Root>/pacemaker' */
static void paceMakerModel_group10_A_Pace(const real_T FXOS87006AxesSensor[3])
{
  paceMakerModel_group10_B.e_PACE_CHARGE_CTRL = 0;
  paceMakerModel_group10_B.e_ATR_GND_CTRL = 0;
  paceMakerModel_group10_B.e_ATR_PACE_CTRL = 1;
  paceMakerModel_group10_B.u = (uint32_T)ceil
    (paceMakerModel_group10_DW.e_PULSE_WIDTH);
  if (((paceMakerModel_group10_B.e_MODE == 0) ||
       (paceMakerModel_group10_B.e_MODE == 2)) &&
      (paceMakerModel_group10_DW.temporalCounter_i1 >=
       paceMakerModel_group10_B.u)) {
    paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
      paceMakerModel_grou_IN_A_Charge;
    paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
    paceMaker_enter_atomic_A_Charge();
  } else if (((paceMakerModel_group10_B.e_MODE == 4) ||
              (paceMakerModel_group10_B.e_MODE == 14)) &&
             (paceMakerModel_group10_DW.temporalCounter_i1 >= (uint32_T)ceil
              (paceMakerModel_group10_B.e_ATR_PULSE_WIDTH))) {
    paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
      paceMakerModel_grou_IN_V_Charge;
    paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
    paceMaker_enter_atomic_V_Charge();
  } else if (paceMakerModel_group10_B.e_input_ready != 0) {
    paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
      paceMakerModel_gr_IN_MODE_CHECK;
    paceMak_enter_atomic_MODE_CHECK();
  } else {
    if (((paceMakerModel_group10_B.e_MODE == 10) ||
         (paceMakerModel_group10_B.e_MODE == 12)) &&
        (paceMakerModel_group10_DW.temporalCounter_i1 >=
         paceMakerModel_group10_B.u)) {
      paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
        paceMakerMod_IN_RATE_MODULATION;
      pa_enter_atomic_RATE_MODULATION(FXOS87006AxesSensor);
    }
  }
}

static void p_SystemCore_rele_p(const freedomk64f_SCIRead_paceMaker_T *obj)
{
  if ((obj->isInitialized == 1) && obj->isSetupComplete) {
    MW_SCI_Close(obj->MW_SCIHANDLE);
  }
}

static void p_SystemCore_dele_p(const freedomk64f_SCIRead_paceMaker_T *obj)
{
  p_SystemCore_rele_p(obj);
}

static void paceMakerMode_matlabCodegenHa_p(freedomk64f_SCIRead_paceMaker_T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    p_SystemCore_dele_p(obj);
  }
}

static void p_SystemCore_release_pbmd0kqiuc(const
  freedomk64f_fxos8700_paceMake_T *obj)
{
  if ((obj->isInitialized == 1) && obj->isSetupComplete) {
    MW_I2C_Close(obj->i2cobj.MW_I2C_HANDLE);
  }
}

static void pa_SystemCore_delete_pbmd0kqiuc(const
  freedomk64f_fxos8700_paceMake_T *obj)
{
  p_SystemCore_release_pbmd0kqiuc(obj);
}

static void matlabCodegenHandle__pbmd0kqiuc(freedomk64f_fxos8700_paceMake_T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    pa_SystemCore_delete_pbmd0kqiuc(obj);
  }
}

static void SystemCore_release_pbmd0kqiuc0(b_freedomk64f_I2CMasterWrite__T *obj)
{
  if (obj->isInitialized == 1) {
    obj->isInitialized = 2;
  }
}

static void p_SystemCore_delete_pbmd0kqiuc0(b_freedomk64f_I2CMasterWrite__T *obj)
{
  SystemCore_release_pbmd0kqiuc0(obj);
}

static void matlabCodegenHandle_pbmd0kqiuc0(b_freedomk64f_I2CMasterWrite__T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    p_SystemCore_delete_pbmd0kqiuc0(obj);
  }
}

static void paceMa_SystemCore_release_pbmd0(const
  freedomk64f_DigitalRead_paceM_T *obj)
{
  if ((obj->isInitialized == 1) && obj->isSetupComplete) {
    MW_digitalIO_close(obj->MW_DIGITALIO_HANDLE);
  }
}

static void paceMak_SystemCore_delete_pbmd0(const
  freedomk64f_DigitalRead_paceM_T *obj)
{
  paceMa_SystemCore_release_pbmd0(obj);
}

static void matlabCodegenHandle_matla_pbmd0(freedomk64f_DigitalRead_paceM_T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    paceMak_SystemCore_delete_pbmd0(obj);
  }
}

static void paceMaker_SystemCore_release_pb(const
  freedomk64f_DigitalWrite_pace_T *obj)
{
  if ((obj->isInitialized == 1) && obj->isSetupComplete) {
    MW_digitalIO_close(obj->MW_DIGITALIO_HANDLE);
  }
}

static void paceMakerM_SystemCore_delete_pb(const
  freedomk64f_DigitalWrite_pace_T *obj)
{
  paceMaker_SystemCore_release_pb(obj);
}

static void matlabCodegenHandle_matlabCo_pb(freedomk64f_DigitalWrite_pace_T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    paceMakerM_SystemCore_delete_pb(obj);
  }
}

static void paceMakerM_SystemCore_release_p(const
  freedomk64f_PWMOutput_paceMak_T *obj)
{
  if ((obj->isInitialized == 1) && obj->isSetupComplete) {
    MW_PWM_Stop(obj->MW_PWM_HANDLE);
    MW_PWM_Close(obj->MW_PWM_HANDLE);
  }
}

static void paceMakerMo_SystemCore_delete_p(const
  freedomk64f_PWMOutput_paceMak_T *obj)
{
  paceMakerM_SystemCore_release_p(obj);
}

static void matlabCodegenHandle_matlabCod_p(freedomk64f_PWMOutput_paceMak_T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    paceMakerMo_SystemCore_delete_p(obj);
  }
}

static void paceMakerMo_SystemCore_setup_pb(freedomk64f_SCIRead_paceMaker_T *obj)
{
  obj->isSetupComplete = false;
  obj->isInitialized = 1;
  paceMakerModel_group10_B.TxPinLoc = MW_UNDEFINED_VALUE;
  paceMakerModel_group10_B.SCIModuleLoc = 0;
  obj->MW_SCIHANDLE = MW_SCI_Open(&paceMakerModel_group10_B.SCIModuleLoc, false,
    10U, paceMakerModel_group10_B.TxPinLoc);
  MW_SCI_SetBaudrate(obj->MW_SCIHANDLE, 115200U);
  paceMakerModel_group10_B.StopBitsValue = MW_SCI_STOPBITS_1;
  paceMakerModel_group10_B.ParityValue = MW_SCI_PARITY_NONE;
  MW_SCI_SetFrameFormat(obj->MW_SCIHANDLE, 8,
                        paceMakerModel_group10_B.ParityValue,
                        paceMakerModel_group10_B.StopBitsValue);
  obj->isSetupComplete = true;
}

static void paceMakerMod_SystemCore_setup_p(freedomk64f_fxos8700_paceMake_T *obj)
{
  obj->isSetupComplete = false;
  obj->isInitialized = 1;
  paceMakerModel_group10_B.ModeType = MW_I2C_MASTER;
  paceMakerModel_group10_B.i2cname = 0;
  obj->i2cobj.MW_I2C_HANDLE = MW_I2C_Open(paceMakerModel_group10_B.i2cname,
    paceMakerModel_group10_B.ModeType);
  obj->i2cobj.BusSpeed = 100000U;
  MW_I2C_SetBusSpeed(obj->i2cobj.MW_I2C_HANDLE, obj->i2cobj.BusSpeed);
  paceMakerModel_group10_B.b_SwappedDataBytes[0] = 43U;
  paceMakerModel_group10_B.b_SwappedDataBytes[1] = 64U;
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U,
                     paceMakerModel_group10_B.b_SwappedDataBytes, 2U, false,
                     false);
  OSA_TimeDelay(500U);
  paceMakerModel_group10_B.status = 42U;
  paceMakerModel_group10_B.status = MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE,
    29U, &paceMakerModel_group10_B.status, 1U, true, false);
  if (0 == paceMakerModel_group10_B.status) {
    MW_I2C_MasterRead(obj->i2cobj.MW_I2C_HANDLE, 29U,
                      &paceMakerModel_group10_B.status, 1U, false, true);
    memcpy((void *)&paceMakerModel_group10_B.b_RegisterValue, (void *)
           &paceMakerModel_group10_B.status, (uint32_T)((size_t)1 * sizeof
            (uint8_T)));
  } else {
    paceMakerModel_group10_B.b_RegisterValue = 0U;
  }

  paceMakerModel_group10_B.b_SwappedDataBytes[0] = 42U;
  paceMakerModel_group10_B.b_SwappedDataBytes[1] = (uint8_T)
    (paceMakerModel_group10_B.b_RegisterValue & 254);
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U,
                     paceMakerModel_group10_B.b_SwappedDataBytes, 2U, false,
                     false);
  paceMakerModel_group10_B.b_SwappedDataBytes[0] = 14U;
  paceMakerModel_group10_B.b_SwappedDataBytes[1] = 1U;
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U,
                     paceMakerModel_group10_B.b_SwappedDataBytes, 2U, false,
                     false);
  paceMakerModel_group10_B.b_SwappedDataBytes[0] = 91U;
  paceMakerModel_group10_B.b_SwappedDataBytes[1] = 0U;
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U,
                     paceMakerModel_group10_B.b_SwappedDataBytes, 2U, false,
                     false);
  paceMakerModel_group10_B.b_SwappedDataBytes[0] = 42U;
  paceMakerModel_group10_B.b_SwappedDataBytes[1] = 25U;
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U,
                     paceMakerModel_group10_B.b_SwappedDataBytes, 2U, false,
                     false);
  obj->isSetupComplete = true;
}

/* Model step function */
void paceMakerModel_group10_step(void)
{
  boolean_T tmp;
  boolean_T tmp_0;
  uint8_T status;
  uint8_T y[2];
  uint8_T b_x[2];
  int16_T tmp_1;

  /* MATLABSystem: '<S6>/Serial Receive' */
  if (paceMakerModel_group10_DW.obj_p.SampleTime !=
      paceMakerModel_group10_P.SerialReceive_SampleTime) {
    paceMakerModel_group10_DW.obj_p.SampleTime =
      paceMakerModel_group10_P.SerialReceive_SampleTime;
  }

  status = MW_SCI_Receive(paceMakerModel_group10_DW.obj_p.MW_SCIHANDLE,
    paceMakerModel_group10_B.RxDataLocChar, 54U);
  memcpy((void *)&paceMakerModel_group10_B.SerialReceive_o1[0], (void *)
         &paceMakerModel_group10_B.RxDataLocChar[0], (uint32_T)((size_t)54 *
          sizeof(uint8_T)));

  /* Chart: '<Root>/DCM_comm' incorporates:
   *  MATLABSystem: '<S6>/Serial Receive'
   */
  if (paceMakerModel_group10_DW.is_active_c3_paceMakerModel_gro == 0U) {
    paceMakerModel_group10_DW.is_active_c3_paceMakerModel_gro = 1U;
    paceMakerModel_group10_DW.is_c3_paceMakerModel_group10 =
      paceMakerModel_gro_IN_comm_init;
    paceMakerModel_group10_DW.e_send_req = 0U;
  } else {
    switch (paceMakerModel_group10_DW.is_c3_paceMakerModel_group10) {
     case paceMakerModel_gro_IN_comm_init:
      paceMakerModel_group10_DW.is_c3_paceMakerModel_group10 =
        paceMakerModel__IN_status_check;
      paceMakerModel_group10_B.e_input_ready = 0U;
      break;

     case paceMakerModel_group_IN_receive:
      if (paceMakerModel_group10_DW.e_send_req == 0) {
        paceMakerModel_group10_DW.is_c3_paceMakerModel_group10 =
          paceMakerModel__IN_status_check;
        paceMakerModel_group10_B.e_input_ready = 0U;
      } else {
        if (paceMakerModel_group10_DW.e_send_req != 0) {
          paceMakerModel_group10_DW.is_c3_paceMakerModel_group10 =
            paceMakerModel_gr_IN_send_egram;
          egram_out();
        }
      }
      break;

     case paceMakerModel_gr_IN_send_egram:
      if (status != 0) {
        paceMakerModel_group10_DW.is_c3_paceMakerModel_group10 =
          paceMakerModel__IN_status_check;
        paceMakerModel_group10_B.e_input_ready = 0U;
      } else {
        paceMakerModel_group10_DW.is_c3_paceMakerModel_group10 =
          paceMakerModel_group_IN_receive;
        paceMakerM_enter_atomic_receive
          (paceMakerModel_group10_B.SerialReceive_o1);
      }
      break;

     default:
      /* case IN_status_check: */
      if (status == 0) {
        paceMakerModel_group10_DW.is_c3_paceMakerModel_group10 =
          paceMakerModel_group_IN_receive;
        paceMakerM_enter_atomic_receive
          (paceMakerModel_group10_B.SerialReceive_o1);
      } else {
        if (paceMakerModel_group10_DW.e_send_req != 0) {
          paceMakerModel_group10_DW.is_c3_paceMakerModel_group10 =
            paceMakerModel_gr_IN_send_egram;
          egram_out();
        }
      }
      break;
    }
  }

  /* End of Chart: '<Root>/DCM_comm' */

  /* MATLABSystem: '<S3>/FXOS8700 6-Axes Sensor' */
  if (paceMakerModel_group10_DW.obj.SampleTime !=
      paceMakerModel_group10_P.FXOS87006AxesSensor_SampleTime) {
    paceMakerModel_group10_DW.obj.SampleTime =
      paceMakerModel_group10_P.FXOS87006AxesSensor_SampleTime;
  }

  status = 1U;
  status = MW_I2C_MasterWrite(paceMakerModel_group10_DW.obj.i2cobj.MW_I2C_HANDLE,
    29U, &status, 1U, true, false);
  if (0 == status) {
    MW_I2C_MasterRead(paceMakerModel_group10_DW.obj.i2cobj.MW_I2C_HANDLE, 29U,
                      paceMakerModel_group10_B.output_raw, 6U, false, true);
    memcpy((void *)&paceMakerModel_group10_B.b_output[0], (void *)
           &paceMakerModel_group10_B.output_raw[0], (uint32_T)((size_t)3 *
            sizeof(int16_T)));
    memcpy((void *)&y[0], (void *)&paceMakerModel_group10_B.b_output[0],
           (uint32_T)((size_t)2 * sizeof(uint8_T)));
    b_x[0] = y[1];
    b_x[1] = y[0];
    memcpy((void *)&paceMakerModel_group10_B.b_output[0], (void *)&b_x[0],
           (uint32_T)((size_t)1 * sizeof(int16_T)));
    memcpy((void *)&y[0], (void *)&paceMakerModel_group10_B.b_output[1],
           (uint32_T)((size_t)2 * sizeof(uint8_T)));
    b_x[0] = y[1];
    b_x[1] = y[0];
    memcpy((void *)&paceMakerModel_group10_B.b_output[1], (void *)&b_x[0],
           (uint32_T)((size_t)1 * sizeof(int16_T)));
    memcpy((void *)&y[0], (void *)&paceMakerModel_group10_B.b_output[2],
           (uint32_T)((size_t)2 * sizeof(uint8_T)));
    b_x[0] = y[1];
    b_x[1] = y[0];
    memcpy((void *)&paceMakerModel_group10_B.b_output[2], (void *)&b_x[0],
           (uint32_T)((size_t)1 * sizeof(int16_T)));
  } else {
    paceMakerModel_group10_B.b_output[0] = 0;
    paceMakerModel_group10_B.b_output[1] = 0;
    paceMakerModel_group10_B.b_output[2] = 0;
  }

  paceMakerModel_group10_B.FXOS87006AxesSensor[0] = (real_T)(int16_T)
    (paceMakerModel_group10_B.b_output[0] >> 2) * 2.0 * 0.244 / 1000.0;
  paceMakerModel_group10_B.FXOS87006AxesSensor[1] = (real_T)(int16_T)
    (paceMakerModel_group10_B.b_output[1] >> 2) * 2.0 * 0.244 / 1000.0;
  paceMakerModel_group10_B.FXOS87006AxesSensor[2] = (real_T)(int16_T)
    (paceMakerModel_group10_B.b_output[2] >> 2) * 2.0 * 0.244 / 1000.0;

  /* End of MATLABSystem: '<S3>/FXOS8700 6-Axes Sensor' */

  /* MATLABSystem: '<S1>/ATR_CMP_DETECT' */
  if (paceMakerModel_group10_DW.obj_e.SampleTime !=
      paceMakerModel_group10_P.ATR_CMP_DETECT_SampleTime) {
    paceMakerModel_group10_DW.obj_e.SampleTime =
      paceMakerModel_group10_P.ATR_CMP_DETECT_SampleTime;
  }

  tmp = MW_digitalIO_read(paceMakerModel_group10_DW.obj_e.MW_DIGITALIO_HANDLE);

  /* MATLABSystem: '<S4>/VENT_CMP_DETECT' */
  if (paceMakerModel_group10_DW.obj_d.SampleTime !=
      paceMakerModel_group10_P.VENT_CMP_DETECT_SampleTime) {
    paceMakerModel_group10_DW.obj_d.SampleTime =
      paceMakerModel_group10_P.VENT_CMP_DETECT_SampleTime;
  }

  tmp_0 = MW_digitalIO_read(paceMakerModel_group10_DW.obj_d.MW_DIGITALIO_HANDLE);

  /* Chart: '<Root>/pacemaker' incorporates:
   *  MATLABSystem: '<S1>/ATR_CMP_DETECT'
   *  MATLABSystem: '<S4>/VENT_CMP_DETECT'
   */
  paceMakerModel_group10_B.elapsedTicks =
    paceMakerModel_group10_M->Timing.clockTick0 -
    paceMakerModel_group10_DW.previousTicks;
  paceMakerModel_group10_DW.previousTicks =
    paceMakerModel_group10_M->Timing.clockTick0;
  paceMakerModel_group10_DW.temporalCounter_i1 +=
    paceMakerModel_group10_B.elapsedTicks;
  switch (paceMakerModel_group10_DW.is_c4_paceMakerModel_group10) {
   case paceMakerModel_grou_IN_A_Charge:
    paceMakerModel_group10_A_Charge();
    break;

   case paceMakerModel_group1_IN_A_Pace:
    paceMakerModel_group10_A_Pace(paceMakerModel_group10_B.FXOS87006AxesSensor);
    break;

   case paceMakerModel_group_IN_A_SENSE:
    paceMakerModel_group10_B.d = rt_roundd_snf((real_T)
      paceMakerModel_group10_DW.e_PULSE_INT -
      paceMakerModel_group10_DW.e_PULSE_WIDTH);
    if (paceMakerModel_group10_B.d < 32768.0) {
      if (paceMakerModel_group10_B.d >= -32768.0) {
        tmp_1 = (int16_T)paceMakerModel_group10_B.d;
      } else {
        tmp_1 = MIN_int16_T;
      }
    } else {
      tmp_1 = MAX_int16_T;
    }

    paceMakerModel_group10_B.i = tmp_1 - paceMakerModel_group10_B.e_ARP;
    if (paceMakerModel_group10_B.i > 32767) {
      paceMakerModel_group10_B.i = 32767;
    } else {
      if (paceMakerModel_group10_B.i < -32768) {
        paceMakerModel_group10_B.i = -32768;
      }
    }

    if ((paceMakerModel_group10_DW.temporalCounter_i1 >= (uint32_T)(int16_T)
         paceMakerModel_group10_B.i) && (!tmp)) {
      paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
        paceMakerModel_group1_IN_A_Pace;
      paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
      paceMakerModel_group10_B.e_PACE_CHARGE_CTRL = 0;
      paceMakerModel_group10_B.e_ATR_GND_CTRL = 0;
      paceMakerModel_group10_B.e_ATR_PACE_CTRL = 1;
    } else if (tmp) {
      paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
        paceMakerModel_grou_IN_A_Charge;
      paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
      paceMaker_enter_atomic_A_Charge();
    } else {
      if (paceMakerModel_group10_B.e_input_ready != 0) {
        paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
          paceMakerModel_gr_IN_MODE_CHECK;
        paceMak_enter_atomic_MODE_CHECK();
      }
    }
    break;

   case paceMakerModel_gr_IN_MODE_CHECK:
    if ((paceMakerModel_group10_B.e_MODE == 0) ||
        (paceMakerModel_group10_B.e_MODE == 2) ||
        (paceMakerModel_group10_B.e_MODE == 4) ||
        (paceMakerModel_group10_B.e_MODE == 10) ||
        (paceMakerModel_group10_B.e_MODE == 12) ||
        (paceMakerModel_group10_B.e_MODE == 14)) {
      paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
        paceMakerModel_grou_IN_A_Charge;
      paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
      paceMaker_enter_atomic_A_Charge();
    } else {
      if ((paceMakerModel_group10_B.e_MODE == 1) ||
          (paceMakerModel_group10_B.e_MODE == 3) ||
          (paceMakerModel_group10_B.e_MODE == 11) ||
          (paceMakerModel_group10_B.e_MODE == 13)) {
        paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
          paceMakerModel_grou_IN_V_Charge;
        paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
        paceMaker_enter_atomic_V_Charge();
      }
    }
    break;

   case paceMakerMod_IN_RATE_MODULATION:
    if ((paceMakerModel_group10_B.e_MODE == 10) ||
        (paceMakerModel_group10_B.e_MODE == 12) ||
        (paceMakerModel_group10_B.e_MODE == 14)) {
      paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
        paceMakerModel_grou_IN_A_Charge;
      paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
      paceMaker_enter_atomic_A_Charge();
    } else {
      if ((paceMakerModel_group10_B.e_MODE == 11) ||
          (paceMakerModel_group10_B.e_MODE == 13)) {
        paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
          paceMakerModel_grou_IN_V_Charge;
        paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
        paceMaker_enter_atomic_V_Charge();
      }
    }
    break;

   case paceMakerModel_grou_IN_V_Charge:
    paceMakerModel_group10_B.e_PACE_CHARGE_CTRL = 1;
    paceMakerModel_group10_B.e_VENT_GND_CTRL = 1;
    paceMakerModel_group10_B.e_VENT_PACE_CTRL = 0;
    paceMakerModel_group10_B.e_PACE_GND_CTRL = 1;
    paceMakerModel_group10_B.e_ATR_PACE_CTRL = 0;
    paceMakerModel_group10_B.e_ATR_GND_CTRL = 0;
    paceMakerModel_group10_B.e_Z_ATR_CTRL = 0;
    paceMakerModel_group10_B.e_Z_VENT_CTRL = 0;
    if ((paceMakerModel_group10_DW.temporalCounter_i1 >= (uint32_T)
         paceMakerModel_group10_B.e_VRP) && ((paceMakerModel_group10_B.e_MODE ==
          3) || (paceMakerModel_group10_B.e_MODE == 13))) {
      paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
        paceMakerModel_group_IN_V_SENSE;
      paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
    } else {
      paceMakerModel_group10_B.d = rt_roundd_snf((real_T)
        paceMakerModel_group10_DW.e_PULSE_INT -
        paceMakerModel_group10_DW.e_PULSE_WIDTH);
      if (paceMakerModel_group10_B.d < 32768.0) {
        if (paceMakerModel_group10_B.d >= -32768.0) {
          tmp_1 = (int16_T)paceMakerModel_group10_B.d;
        } else {
          tmp_1 = MIN_int16_T;
        }
      } else {
        tmp_1 = MAX_int16_T;
      }

      if ((((paceMakerModel_group10_B.e_MODE == 1) ||
            (paceMakerModel_group10_B.e_MODE == 11)) &&
           (paceMakerModel_group10_DW.temporalCounter_i1 >= (uint32_T)tmp_1)) ||
          (((paceMakerModel_group10_B.e_MODE == 4) ||
            (paceMakerModel_group10_B.e_MODE == 14)) &&
           (paceMakerModel_group10_DW.temporalCounter_i1 >= (uint32_T)
            paceMakerModel_group10_B.e_AV_DELAY))) {
        paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
          paceMakerModel_group1_IN_V_Pace;
        paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
        paceMakerModel_group10_B.e_PACE_CHARGE_CTRL = 0;
        paceMakerModel_group10_B.e_VENT_GND_CTRL = 0;
        paceMakerModel_group10_B.e_VENT_PACE_CTRL = 1;
      } else {
        if (paceMakerModel_group10_B.e_input_ready != 0) {
          paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
            paceMakerModel_gr_IN_MODE_CHECK;
          paceMak_enter_atomic_MODE_CHECK();
        }
      }
    }
    break;

   case paceMakerModel_group1_IN_V_Pace:
    paceMakerModel_group10_B.e_PACE_CHARGE_CTRL = 0;
    paceMakerModel_group10_B.e_VENT_GND_CTRL = 0;
    paceMakerModel_group10_B.e_VENT_PACE_CTRL = 1;
    paceMakerModel_group10_B.elapsedTicks = (uint32_T)ceil
      (paceMakerModel_group10_DW.e_PULSE_WIDTH);
    if (((paceMakerModel_group10_B.e_MODE == 1) ||
         (paceMakerModel_group10_B.e_MODE == 3)) &&
        (paceMakerModel_group10_DW.temporalCounter_i1 >=
         paceMakerModel_group10_B.elapsedTicks)) {
      paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
        paceMakerModel_grou_IN_V_Charge;
      paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
      paceMaker_enter_atomic_V_Charge();
    } else if ((paceMakerModel_group10_B.e_MODE == 4) &&
               (paceMakerModel_group10_DW.temporalCounter_i1 >= (uint32_T)ceil
                (paceMakerModel_group10_B.e_VENT_PULSE_WIDTH))) {
      paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
        paceMakerModel_grou_IN_A_Charge;
      paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
      paceMaker_enter_atomic_A_Charge();
    } else if (paceMakerModel_group10_B.e_input_ready != 0) {
      paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
        paceMakerModel_gr_IN_MODE_CHECK;
      paceMak_enter_atomic_MODE_CHECK();
    } else {
      if (((paceMakerModel_group10_B.e_MODE == 11) ||
           (paceMakerModel_group10_B.e_MODE == 13) ||
           (paceMakerModel_group10_B.e_MODE == 14)) &&
          (paceMakerModel_group10_DW.temporalCounter_i1 >=
           paceMakerModel_group10_B.elapsedTicks)) {
        paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
          paceMakerMod_IN_RATE_MODULATION;
        pa_enter_atomic_RATE_MODULATION
          (paceMakerModel_group10_B.FXOS87006AxesSensor);
      }
    }
    break;

   default:
    /* case IN_V_SENSE: */
    if (tmp_0) {
      paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
        paceMakerModel_grou_IN_V_Charge;
      paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
      paceMaker_enter_atomic_V_Charge();
    } else {
      paceMakerModel_group10_B.d = rt_roundd_snf((real_T)
        paceMakerModel_group10_DW.e_PULSE_INT -
        paceMakerModel_group10_DW.e_PULSE_WIDTH);
      if (paceMakerModel_group10_B.d < 32768.0) {
        if (paceMakerModel_group10_B.d >= -32768.0) {
          tmp_1 = (int16_T)paceMakerModel_group10_B.d;
        } else {
          tmp_1 = MIN_int16_T;
        }
      } else {
        tmp_1 = MAX_int16_T;
      }

      paceMakerModel_group10_B.i = tmp_1 - paceMakerModel_group10_B.e_VRP;
      if (paceMakerModel_group10_B.i > 32767) {
        paceMakerModel_group10_B.i = 32767;
      } else {
        if (paceMakerModel_group10_B.i < -32768) {
          paceMakerModel_group10_B.i = -32768;
        }
      }

      if (paceMakerModel_group10_DW.temporalCounter_i1 >= (uint32_T)(int16_T)
          paceMakerModel_group10_B.i) {
        paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
          paceMakerModel_group1_IN_V_Pace;
        paceMakerModel_group10_DW.temporalCounter_i1 = 0U;
        paceMakerModel_group10_B.e_PACE_CHARGE_CTRL = 0;
        paceMakerModel_group10_B.e_VENT_GND_CTRL = 0;
        paceMakerModel_group10_B.e_VENT_PACE_CTRL = 1;
      } else {
        if (paceMakerModel_group10_B.e_input_ready != 0) {
          paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
            paceMakerModel_gr_IN_MODE_CHECK;
          paceMak_enter_atomic_MODE_CHECK();
        }
      }
    }
    break;
  }

  /* End of Chart: '<Root>/pacemaker' */

  /* MATLABSystem: '<S1>/ATR_GND_CTRL' */
  MW_digitalIO_write(paceMakerModel_group10_DW.obj_h.MW_DIGITALIO_HANDLE,
                     paceMakerModel_group10_B.e_ATR_GND_CTRL != 0);

  /* MATLABSystem: '<S1>/ATR_PACE_CTRL' */
  MW_digitalIO_write(paceMakerModel_group10_DW.obj_ov.MW_DIGITALIO_HANDLE,
                     paceMakerModel_group10_B.e_ATR_PACE_CTRL != 0);

  /* MATLABSystem: '<S1>/Z_ATR_CTRL' */
  MW_digitalIO_write(paceMakerModel_group10_DW.obj_l0.MW_DIGITALIO_HANDLE,
                     paceMakerModel_group10_B.e_Z_ATR_CTRL != 0);

  /* MATLABSystem: '<S3>/PACE_CHARGE_CTRL' */
  MW_digitalIO_write(paceMakerModel_group10_DW.obj_nv.MW_DIGITALIO_HANDLE,
                     paceMakerModel_group10_B.e_PACE_CHARGE_CTRL != 0);

  /* MATLABSystem: '<S3>/PACE_GND_CTRL' */
  MW_digitalIO_write(paceMakerModel_group10_DW.obj_b.MW_DIGITALIO_HANDLE,
                     paceMakerModel_group10_B.e_PACE_GND_CTRL != 0);

  /* MATLABSystem: '<S3>/PACING_REF_PWM' incorporates:
   *  Gain: '<S3>/Gain'
   */
  MW_PWM_SetDutyCycle(paceMakerModel_group10_DW.obj_i.MW_PWM_HANDLE, (real_T)
                      (paceMakerModel_group10_P.Gain_Gain *
                       paceMakerModel_group10_B.e_PACING_REF_PWM));

  /* MATLABSystem: '<S4>/VENT_GND_CTRL' */
  MW_digitalIO_write(paceMakerModel_group10_DW.obj_l.MW_DIGITALIO_HANDLE,
                     paceMakerModel_group10_B.e_VENT_GND_CTRL != 0);

  /* MATLABSystem: '<S4>/VENT_PACE_CTRL' */
  MW_digitalIO_write(paceMakerModel_group10_DW.obj_o.MW_DIGITALIO_HANDLE,
                     paceMakerModel_group10_B.e_VENT_PACE_CTRL != 0);

  /* MATLABSystem: '<S4>/Z_VENT_CTRL' */
  MW_digitalIO_write(paceMakerModel_group10_DW.obj_g.MW_DIGITALIO_HANDLE,
                     paceMakerModel_group10_B.e_Z_VENT_CTRL != 0);

  /* MATLABSystem: '<S1>/ATR_CMP_REF_PWM' incorporates:
   *  Gain: '<S1>/Gain'
   */
  MW_PWM_SetDutyCycle(paceMakerModel_group10_DW.obj_n.MW_PWM_HANDLE, (real_T)
                      (paceMakerModel_group10_P.Gain_Gain_o *
                       paceMakerModel_group10_B.e_ATR_CMP_REF) * 0.125);

  /* MATLABSystem: '<S4>/VENT_CMP_REF_PWM' incorporates:
   *  Gain: '<S4>/Gain'
   */
  MW_PWM_SetDutyCycle(paceMakerModel_group10_DW.obj_ds.MW_PWM_HANDLE, (real_T)
                      (paceMakerModel_group10_P.Gain_Gain_i *
                       paceMakerModel_group10_B.e_VENT_CMP_REF) * 0.125);

  /* MATLABSystem: '<S3>/FRONT_CTRL' incorporates:
   *  Constant: '<S3>/Constant'
   */
  MW_digitalIO_write(paceMakerModel_group10_DW.obj_n4.MW_DIGITALIO_HANDLE,
                     paceMakerModel_group10_P.Constant_Value != 0.0);

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The resolution of this integer timer is 0.001, which is the step size
   * of the task. Size of "clockTick0" ensures timer will not overflow during the
   * application lifespan selected.
   */
  paceMakerModel_group10_M->Timing.clockTick0++;
}

/* Model initialize function */
void paceMakerModel_group10_initialize(void)
{
  {
    freedomk64f_fxos8700_paceMake_T *obj;
    freedomk64f_DigitalRead_paceM_T *obj_0;
    freedomk64f_DigitalWrite_pace_T *obj_1;
    freedomk64f_PWMOutput_paceMak_T *obj_2;

    /* SystemInitialize for S-Function (sfun_private_function_caller) generated from: '<S6>/Simulink Function' incorporates:
     *  SubSystem: '<S6>/Simulink Function'
     */
    egram_out_Init();

    /* End of SystemInitialize for S-Function (sfun_private_function_caller) generated from: '<S6>/Simulink Function' */

    /* Chart: '<Root>/pacemaker' */
    paceMakerModel_group10_DW.is_c4_paceMakerModel_group10 =
      paceMakerModel_gr_IN_MODE_CHECK;
    paceMak_enter_atomic_MODE_CHECK();

    /* Start for MATLABSystem: '<S6>/Serial Receive' */
    paceMakerModel_group10_DW.obj_p.isInitialized = 0;
    paceMakerModel_group10_DW.obj_p.matlabCodegenIsDeleted = false;
    paceMakerModel_group10_DW.obj_p.SampleTime =
      paceMakerModel_group10_P.SerialReceive_SampleTime;
    paceMakerMo_SystemCore_setup_pb(&paceMakerModel_group10_DW.obj_p);

    /* Start for MATLABSystem: '<S3>/FXOS8700 6-Axes Sensor' */
    paceMakerModel_group10_DW.obj.i2cobj.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj.matlabCodegenIsDeleted = true;
    obj = &paceMakerModel_group10_DW.obj;
    paceMakerModel_group10_DW.obj.isInitialized = 0;
    paceMakerModel_group10_DW.obj.SampleTime = -1.0;
    obj->i2cobj.isInitialized = 0;
    obj->i2cobj.matlabCodegenIsDeleted = false;
    paceMakerModel_group10_DW.obj.matlabCodegenIsDeleted = false;
    paceMakerModel_group10_DW.obj.SampleTime =
      paceMakerModel_group10_P.FXOS87006AxesSensor_SampleTime;
    paceMakerMod_SystemCore_setup_p(&paceMakerModel_group10_DW.obj);

    /* Start for MATLABSystem: '<S1>/ATR_CMP_DETECT' */
    paceMakerModel_group10_DW.obj_e.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_e.isInitialized = 0;
    paceMakerModel_group10_DW.obj_e.SampleTime = -1.0;
    paceMakerModel_group10_DW.obj_e.matlabCodegenIsDeleted = false;
    paceMakerModel_group10_DW.obj_e.SampleTime =
      paceMakerModel_group10_P.ATR_CMP_DETECT_SampleTime;
    obj_0 = &paceMakerModel_group10_DW.obj_e;
    paceMakerModel_group10_DW.obj_e.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_e.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(0U, 0);
    paceMakerModel_group10_DW.obj_e.isSetupComplete = true;

    /* Start for MATLABSystem: '<S4>/VENT_CMP_DETECT' */
    paceMakerModel_group10_DW.obj_d.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_d.isInitialized = 0;
    paceMakerModel_group10_DW.obj_d.SampleTime = -1.0;
    paceMakerModel_group10_DW.obj_d.matlabCodegenIsDeleted = false;
    paceMakerModel_group10_DW.obj_d.SampleTime =
      paceMakerModel_group10_P.VENT_CMP_DETECT_SampleTime;
    obj_0 = &paceMakerModel_group10_DW.obj_d;
    paceMakerModel_group10_DW.obj_d.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_d.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(1U, 0);
    paceMakerModel_group10_DW.obj_d.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/ATR_GND_CTRL' */
    paceMakerModel_group10_DW.obj_h.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_h.isInitialized = 0;
    paceMakerModel_group10_DW.obj_h.matlabCodegenIsDeleted = false;
    obj_1 = &paceMakerModel_group10_DW.obj_h;
    paceMakerModel_group10_DW.obj_h.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_h.isInitialized = 1;
    obj_1->MW_DIGITALIO_HANDLE = MW_digitalIO_open(11U, 1);
    paceMakerModel_group10_DW.obj_h.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/ATR_PACE_CTRL' */
    paceMakerModel_group10_DW.obj_ov.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_ov.isInitialized = 0;
    paceMakerModel_group10_DW.obj_ov.matlabCodegenIsDeleted = false;
    obj_1 = &paceMakerModel_group10_DW.obj_ov;
    paceMakerModel_group10_DW.obj_ov.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_ov.isInitialized = 1;
    obj_1->MW_DIGITALIO_HANDLE = MW_digitalIO_open(8U, 1);
    paceMakerModel_group10_DW.obj_ov.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/Z_ATR_CTRL' */
    paceMakerModel_group10_DW.obj_l0.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_l0.isInitialized = 0;
    paceMakerModel_group10_DW.obj_l0.matlabCodegenIsDeleted = false;
    obj_1 = &paceMakerModel_group10_DW.obj_l0;
    paceMakerModel_group10_DW.obj_l0.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_l0.isInitialized = 1;
    obj_1->MW_DIGITALIO_HANDLE = MW_digitalIO_open(4U, 1);
    paceMakerModel_group10_DW.obj_l0.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/PACE_CHARGE_CTRL' */
    paceMakerModel_group10_DW.obj_nv.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_nv.isInitialized = 0;
    paceMakerModel_group10_DW.obj_nv.matlabCodegenIsDeleted = false;
    obj_1 = &paceMakerModel_group10_DW.obj_nv;
    paceMakerModel_group10_DW.obj_nv.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_nv.isInitialized = 1;
    obj_1->MW_DIGITALIO_HANDLE = MW_digitalIO_open(2U, 1);
    paceMakerModel_group10_DW.obj_nv.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/PACE_GND_CTRL' */
    paceMakerModel_group10_DW.obj_b.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_b.isInitialized = 0;
    paceMakerModel_group10_DW.obj_b.matlabCodegenIsDeleted = false;
    obj_1 = &paceMakerModel_group10_DW.obj_b;
    paceMakerModel_group10_DW.obj_b.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_b.isInitialized = 1;
    obj_1->MW_DIGITALIO_HANDLE = MW_digitalIO_open(10U, 1);
    paceMakerModel_group10_DW.obj_b.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/PACING_REF_PWM' */
    paceMakerModel_group10_DW.obj_i.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_i.isInitialized = 0;
    paceMakerModel_group10_DW.obj_i.matlabCodegenIsDeleted = false;
    obj_2 = &paceMakerModel_group10_DW.obj_i;
    paceMakerModel_group10_DW.obj_i.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_i.isInitialized = 1;
    obj_2->MW_PWM_HANDLE = MW_PWM_Open(5U, 2000.0, 0.0);
    MW_PWM_Start(paceMakerModel_group10_DW.obj_i.MW_PWM_HANDLE);
    paceMakerModel_group10_DW.obj_i.isSetupComplete = true;

    /* Start for MATLABSystem: '<S4>/VENT_GND_CTRL' */
    paceMakerModel_group10_DW.obj_l.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_l.isInitialized = 0;
    paceMakerModel_group10_DW.obj_l.matlabCodegenIsDeleted = false;
    obj_1 = &paceMakerModel_group10_DW.obj_l;
    paceMakerModel_group10_DW.obj_l.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_l.isInitialized = 1;
    obj_1->MW_DIGITALIO_HANDLE = MW_digitalIO_open(12U, 1);
    paceMakerModel_group10_DW.obj_l.isSetupComplete = true;

    /* Start for MATLABSystem: '<S4>/VENT_PACE_CTRL' */
    paceMakerModel_group10_DW.obj_o.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_o.isInitialized = 0;
    paceMakerModel_group10_DW.obj_o.matlabCodegenIsDeleted = false;
    obj_1 = &paceMakerModel_group10_DW.obj_o;
    paceMakerModel_group10_DW.obj_o.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_o.isInitialized = 1;
    obj_1->MW_DIGITALIO_HANDLE = MW_digitalIO_open(9U, 1);
    paceMakerModel_group10_DW.obj_o.isSetupComplete = true;

    /* Start for MATLABSystem: '<S4>/Z_VENT_CTRL' */
    paceMakerModel_group10_DW.obj_g.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_g.isInitialized = 0;
    paceMakerModel_group10_DW.obj_g.matlabCodegenIsDeleted = false;
    obj_1 = &paceMakerModel_group10_DW.obj_g;
    paceMakerModel_group10_DW.obj_g.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_g.isInitialized = 1;
    obj_1->MW_DIGITALIO_HANDLE = MW_digitalIO_open(7U, 1);
    paceMakerModel_group10_DW.obj_g.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/ATR_CMP_REF_PWM' */
    paceMakerModel_group10_DW.obj_n.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_n.isInitialized = 0;
    paceMakerModel_group10_DW.obj_n.matlabCodegenIsDeleted = false;
    obj_2 = &paceMakerModel_group10_DW.obj_n;
    paceMakerModel_group10_DW.obj_n.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_n.isInitialized = 1;
    obj_2->MW_PWM_HANDLE = MW_PWM_Open(6U, 2000.0, 0.0);
    MW_PWM_Start(paceMakerModel_group10_DW.obj_n.MW_PWM_HANDLE);
    paceMakerModel_group10_DW.obj_n.isSetupComplete = true;

    /* Start for MATLABSystem: '<S4>/VENT_CMP_REF_PWM' */
    paceMakerModel_group10_DW.obj_ds.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_ds.isInitialized = 0;
    paceMakerModel_group10_DW.obj_ds.matlabCodegenIsDeleted = false;
    obj_2 = &paceMakerModel_group10_DW.obj_ds;
    paceMakerModel_group10_DW.obj_ds.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_ds.isInitialized = 1;
    obj_2->MW_PWM_HANDLE = MW_PWM_Open(3U, 2000.0, 0.0);
    MW_PWM_Start(paceMakerModel_group10_DW.obj_ds.MW_PWM_HANDLE);
    paceMakerModel_group10_DW.obj_ds.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/FRONT_CTRL' */
    paceMakerModel_group10_DW.obj_n4.matlabCodegenIsDeleted = true;
    paceMakerModel_group10_DW.obj_n4.isInitialized = 0;
    paceMakerModel_group10_DW.obj_n4.matlabCodegenIsDeleted = false;
    obj_1 = &paceMakerModel_group10_DW.obj_n4;
    paceMakerModel_group10_DW.obj_n4.isSetupComplete = false;
    paceMakerModel_group10_DW.obj_n4.isInitialized = 1;
    obj_1->MW_DIGITALIO_HANDLE = MW_digitalIO_open(13U, 1);
    paceMakerModel_group10_DW.obj_n4.isSetupComplete = true;

    /* Enable for Chart: '<Root>/pacemaker' */
    paceMakerModel_group10_DW.previousTicks =
      paceMakerModel_group10_M->Timing.clockTick0;
  }
}

/* Model terminate function */
void paceMakerModel_group10_terminate(void)
{
  /* Terminate for MATLABSystem: '<S6>/Serial Receive' */
  paceMakerMode_matlabCodegenHa_p(&paceMakerModel_group10_DW.obj_p);

  /* Terminate for S-Function (sfun_private_function_caller) generated from: '<S6>/Simulink Function' incorporates:
   *  SubSystem: '<S6>/Simulink Function'
   */
  egram_out_Term();

  /* End of Terminate for S-Function (sfun_private_function_caller) generated from: '<S6>/Simulink Function' */

  /* Terminate for MATLABSystem: '<S3>/FXOS8700 6-Axes Sensor' */
  matlabCodegenHandle__pbmd0kqiuc(&paceMakerModel_group10_DW.obj);
  matlabCodegenHandle_pbmd0kqiuc0(&paceMakerModel_group10_DW.obj.i2cobj);

  /* Terminate for MATLABSystem: '<S1>/ATR_CMP_DETECT' */
  matlabCodegenHandle_matla_pbmd0(&paceMakerModel_group10_DW.obj_e);

  /* Terminate for MATLABSystem: '<S4>/VENT_CMP_DETECT' */
  matlabCodegenHandle_matla_pbmd0(&paceMakerModel_group10_DW.obj_d);

  /* Terminate for MATLABSystem: '<S1>/ATR_GND_CTRL' */
  matlabCodegenHandle_matlabCo_pb(&paceMakerModel_group10_DW.obj_h);

  /* Terminate for MATLABSystem: '<S1>/ATR_PACE_CTRL' */
  matlabCodegenHandle_matlabCo_pb(&paceMakerModel_group10_DW.obj_ov);

  /* Terminate for MATLABSystem: '<S1>/Z_ATR_CTRL' */
  matlabCodegenHandle_matlabCo_pb(&paceMakerModel_group10_DW.obj_l0);

  /* Terminate for MATLABSystem: '<S3>/PACE_CHARGE_CTRL' */
  matlabCodegenHandle_matlabCo_pb(&paceMakerModel_group10_DW.obj_nv);

  /* Terminate for MATLABSystem: '<S3>/PACE_GND_CTRL' */
  matlabCodegenHandle_matlabCo_pb(&paceMakerModel_group10_DW.obj_b);

  /* Terminate for MATLABSystem: '<S3>/PACING_REF_PWM' */
  matlabCodegenHandle_matlabCod_p(&paceMakerModel_group10_DW.obj_i);

  /* Terminate for MATLABSystem: '<S4>/VENT_GND_CTRL' */
  matlabCodegenHandle_matlabCo_pb(&paceMakerModel_group10_DW.obj_l);

  /* Terminate for MATLABSystem: '<S4>/VENT_PACE_CTRL' */
  matlabCodegenHandle_matlabCo_pb(&paceMakerModel_group10_DW.obj_o);

  /* Terminate for MATLABSystem: '<S4>/Z_VENT_CTRL' */
  matlabCodegenHandle_matlabCo_pb(&paceMakerModel_group10_DW.obj_g);

  /* Terminate for MATLABSystem: '<S1>/ATR_CMP_REF_PWM' */
  matlabCodegenHandle_matlabCod_p(&paceMakerModel_group10_DW.obj_n);

  /* Terminate for MATLABSystem: '<S4>/VENT_CMP_REF_PWM' */
  matlabCodegenHandle_matlabCod_p(&paceMakerModel_group10_DW.obj_ds);

  /* Terminate for MATLABSystem: '<S3>/FRONT_CTRL' */
  matlabCodegenHandle_matlabCo_pb(&paceMakerModel_group10_DW.obj_n4);
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
