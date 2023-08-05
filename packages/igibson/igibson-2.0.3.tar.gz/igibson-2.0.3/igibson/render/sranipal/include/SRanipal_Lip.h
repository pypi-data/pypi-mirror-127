///////////////////////////////////////////////////////////////////////////////////////
//
//  IMPORTANT: READ BEFORE DOWNLOADING, COPYING, INSTALLING OR USING.
//
//  By downloading, copying, installing or using the software you agree to this license.
//  If you do not agree to this license, do not download, install,
//  copy or use the software.
//
//                           License Agreement
//                     For Vive Super Reality Library
//
// Copyright (c) 2017,		HTC Corporation
//
// All rights reserved. Third party copyrights are property of their respective owners.
//
// Redistribution and use in source and binary forms, with or without modification,
// are permitted provided that the following conditions are met:
//
//   * Redistribution's of source code must retain the above copyright notice,
//     this list of conditions and the following disclaimer.
//
//   * Redistribution's in binary form must reproduce the above copyright notice,
//     this list of conditions and the following disclaimer in the documentation
//     and/or other materials provided with the distribution.
//
//   * The name of the copyright holders may not be used to endorse or promote products
//     derived from this software without specific prior written permission.
//
// This software is provided by the copyright holders and contributors "as is" and
// any express or implied warranties, including, but not limited to, the implied
// warranties of merchantability and fitness for a particular purpose are disclaimed.
// In no event shall the Intel Corporation or contributors be liable for any direct,
// indirect, incidental, special, exemplary, or consequential damages
// (including, but not limited to, procurement of substitute goods or services;
// loss of use, data, or profits; or business interruption) however caused
// and on any theory of liability, whether in contract, strict liability,
// or tort (including negligence or otherwise) arising in any way out of
// the use of this software, even if advised of the possibility of such damage.
//
///////////////////////////////////////////////////////////////////////////////////////
#pragma once
#include "SRanipal_LipData_v1.h"
#include "SRanipal_LipData_v2.h"
#ifdef SRANIPAL_EXPORTS
#define SR_ANIPAL __declspec(dllexport)
#else
#define SR_ANIPAL __declspec(dllimport)
#endif

extern "C" {

	namespace ViveSR {

		namespace anipal {

			namespace Lip {

				const int ANIPAL_TYPE_LIP = 1;

                const int ANIPAL_TYPE_LIP_V2 = 3;

				/** Gets the LipData from Lip engine.
				* @param data ViveSR::anipal::Lip::LipData
				* @return Indicates the resulting ViveSR::Error status of this method.
				*/
				SR_ANIPAL int GetLipData(LipData *data);

                /** Gets the LipData_v2 from Lip engine. The version 2 LipData contains tongue's blendshape
                * @param data ViveSR::anipal::Lip::LipData_v2
                * @return Indicates the resulting ViveSR::Error status of this method.
                */
                SR_ANIPAL int GetLipData_v2(LipData_v2 *data);
			}
		}
	}
}