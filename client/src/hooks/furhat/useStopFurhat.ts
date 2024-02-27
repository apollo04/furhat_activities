import { AxiosError, AxiosResponse } from 'axios';
import { UseMutationResult, useMutation } from 'react-query';
import { axiosUnauthorizedInstance } from 'utils/request';

export default function useStopFurhat(
  ip: string
): UseMutationResult<AxiosResponse<any>, AxiosError<{ message: string }>, any> {
  const postStopFurhat = () => {
    return axiosUnauthorizedInstance.get(`furhat/${ip}/stop/`);
  };

  return useMutation(postStopFurhat);
}
