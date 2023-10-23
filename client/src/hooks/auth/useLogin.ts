import { AxiosError, AxiosResponse } from 'axios';
import { useMutation, UseMutationResult } from 'react-query';
import { UserLogin } from 'types/generated';
import { axiosUnauthorizedInstance } from 'utils/request';

export default function useLogin(): UseMutationResult<
  AxiosResponse<any>,
  AxiosError<{ message: string }>,
  UserLogin
> {
  const login = (payload: UserLogin) => {
    return axiosUnauthorizedInstance.post('auth/login', payload);
  };
  return useMutation(login);
}
